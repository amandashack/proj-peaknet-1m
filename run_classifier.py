#!/usr/bin/env python3
"""
LCLS Run Classifier with Context-Aware Chunking

This tool classifies LCLS experimental runs using chunking that builds output
incrementally. Each chunk includes preceding runs with their classifications
as context for better consistency and pattern recognition.
"""

import argparse
import json
import time
import os
import sys
import re
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
# from tqdm import tqdm  # Removed dependency
import logging


class StanfordAPIError(Exception):
    """Custom exception for Stanford API errors"""
    pass


class RunClassifier:
    """
    Client for Stanford AI Gateway API calls with context-aware chunking

    Builds output incrementally, chunk by chunk, with preceding runs providing
    rich context including their already-determined classifications.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-7-sonnet"):
        """
        Initialize the API client

        Args:
            api_key: Stanford API key (defaults to STANFORD_API_KEY env var)
            model: Model to use for analysis
        """
        self.api_key = api_key or os.getenv("STANFORD_API_KEY")
        if not self.api_key:
            raise StanfordAPIError("STANFORD_API_KEY environment variable not set")

        self.model = model
        self.base_url = "https://aiapi-prod.stanford.edu/v1"
        self.max_tokens = 8192
        self.temperature = 0.1

        # Setup session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Set default headers
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

        # Setup logging
        self.logger = logging.getLogger(__name__)

        # Token usage tracking
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0
        self.chunk_token_history = []

    def _make_api_call(self, prompt: str, max_retries: int = 3) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Make API call to Stanford AI Gateway with robust error handling"""
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }

        for attempt in range(max_retries):
            try:
                self.logger.debug(f"Making API call (attempt {attempt + 1}/{max_retries})...")

                response = self.session.post(
                    f"{self.base_url}/chat/completions",
                    json=payload,
                    timeout=120
                )

                if response.status_code == 200:
                    try:
                        response_data = response.json()
                        usage = response_data.get('usage', {})
                        return response_data, usage
                    except json.JSONDecodeError as e:
                        error_msg = f"Invalid JSON response: {e}. Raw response: {response.text[:200]}"
                        if attempt < max_retries - 1:
                            self.logger.warning(f"  {error_msg}, retrying...")
                            continue
                        else:
                            raise StanfordAPIError(error_msg)
                else:
                    error_msg = f"API call failed with status {response.status_code}"
                    if response.text:
                        error_msg += f": {response.text}"

                    if attempt < max_retries - 1:
                        self.logger.warning(f"  {error_msg}, retrying...")
                        time.sleep(2 ** attempt)
                        continue
                    else:
                        raise StanfordAPIError(error_msg)

            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    self.logger.warning(f"  Request failed: {e}, retrying...")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    raise StanfordAPIError(f"Request failed after {max_retries} attempts: {e}")

        raise StanfordAPIError("Unexpected error in API call")

    def _validate_response(self, response: Dict[str, Any]) -> str:
        """Validate and extract content from API response"""
        try:
            content = response["choices"][0]["message"]["content"]
            if not content:
                raise StanfordAPIError("API returned empty content")
            return content.strip()
        except (KeyError, IndexError, TypeError) as e:
            raise StanfordAPIError(f"Invalid API response format: {e}")

    def _extract_json_from_response(self, content: str) -> str:
        """Extract JSON from API response content"""
        # Try to find JSON block in markdown code blocks
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', content, re.DOTALL)
        if json_match:
            return json_match.group(1)

        # Try to find standalone JSON object
        json_match = re.search(r'(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})', content, re.DOTALL)
        if json_match:
            return json_match.group(1)

        return content

    def _validate_chunk_classifications(self, json_str: str) -> Dict[str, Any]:
        """Validate JSON output for chunk classifications"""
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            raise StanfordAPIError(f"Invalid JSON response: {e}")

        # Check required top-level fields
        required_fields = ["experiment_id", "chunk_info", "classifications"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise StanfordAPIError(f"Missing required fields: {missing_fields}")

        # Validate classifications array
        if not isinstance(data["classifications"], list):
            raise StanfordAPIError("Classifications must be an array")

        # Check each classification entry
        valid_classifications = {"commissioning_run", "alignment_run", "timing_run", "calibration_run", "measurement_run", "diagnostic_run", "unknown_run"}
        valid_confidence = {"high", "medium", "low"}

        for i, classification in enumerate(data["classifications"]):
            run_fields = ["run_number", "classification", "confidence", "key_evidence"]
            missing_run_fields = [field for field in run_fields if field not in classification]
            if missing_run_fields:
                raise StanfordAPIError(f"Run {i+1} missing required fields: {missing_run_fields}")

            if classification["classification"] not in valid_classifications:
                raise StanfordAPIError(f"Run {classification['run_number']} has invalid classification: {classification['classification']}")

            if classification["confidence"] not in valid_confidence:
                raise StanfordAPIError(f"Run {classification['run_number']} has invalid confidence: {classification['confidence']}")

        return data

    def _parse_experiment_file(self, markdown_content: str) -> Tuple[str, int, List[Dict]]:
        """
        Parse experiment file to extract experiment ID, run count, and run data

        Returns:
            Tuple of (experiment_id, total_runs, run_data_list)
        """
        # Extract experiment ID from header
        exp_match = re.search(r'# Experiment (\w+)', markdown_content)
        if not exp_match:
            raise StanfordAPIError("Could not extract experiment ID from file")
        experiment_id = exp_match.group(1)

        # Parse individual runs with their data
        run_pattern = r'### Run (\d+)\n(.*?)(?=### Run \d+|\Z)'
        runs = re.findall(run_pattern, markdown_content, re.DOTALL)

        run_data = []
        for run_num_str, run_content in runs:
            run_data.append({
                'run_number': int(run_num_str),
                'content': f"### Run {run_num_str}\n{run_content.strip()}"
            })

        return experiment_id, len(run_data), run_data

    def _read_previous_classifications(self, output_file: Path, num_context: int) -> List[Dict]:
        """
        Read the last N classifications from the output file

        Args:
            output_file: Path to the output file
            num_context: Number of previous classifications to read

        Returns:
            List of previous classification dictionaries
        """
        if not output_file.exists():
            return []

        try:
            with open(output_file, 'r') as f:
                data = json.load(f)
                classifications = data.get('classifications', [])
                return classifications[-num_context:] if classifications else []
        except (json.JSONDecodeError, KeyError, IOError):
            return []

    def _create_context_content(self, context_classifications: List[Dict], raw_run_data: List[Dict]) -> str:
        """
        Create context content that includes previous classifications

        Args:
            context_classifications: Previous classification results
            raw_run_data: Raw run data for context runs

        Returns:
            Formatted context content with classifications included
        """
        if not context_classifications:
            return ""

        context_content = []

        # Create a map of run_number to classification for quick lookup
        classification_map = {c['run_number']: c for c in context_classifications}

        for run_data in raw_run_data:
            run_num = run_data['run_number']
            if run_num in classification_map:
                # Include the original content plus the classification
                classification = classification_map[run_num]

                # Replace __ANSWER__ placeholders with actual classifications
                content = run_data['content']
                content = content.replace(
                    "**Run classification**: __ANSWER__",
                    f"**Run classification**: {classification['classification']}"
                )
                content = content.replace(
                    "**Confidence**: __ANSWER__", 
                    f"**Confidence**: {classification['confidence']}"
                )
                content = content.replace(
                    "**Key evidence**: __ANSWER__",
                    f"**Key evidence**: {classification['key_evidence']}"
                )

                # Add context marker
                content = content.replace(
                    f"### Run {run_num}",
                    f"### Run {run_num} (CONTEXT - already classified)"
                )

                context_content.append(content)

        return "\n\n".join(context_content)

    def _create_prompt(self, experiment_id: str, context_content: str, 
                      new_runs: List[Dict], chunk_num: int, total_chunks: int) -> str:
        """Create classification prompt with rich context"""

        # Build new runs content (with __ANSWER__ placeholders)
        new_runs_content = "\n\n".join([run['content'] for run in new_runs])

        # Combine context and new content
        if context_content:
            full_content = f"{context_content}\n\n{new_runs_content}"
            context_note = f"\n\n**CONTEXT NOTE**: Runs marked as 'CONTEXT' are already classified and included for pattern recognition. Only classify the NEW runs ({new_runs[0]['run_number']}-{new_runs[-1]['run_number']})."
        else:
            full_content = new_runs_content
            context_note = ""

        new_run_numbers = [run['run_number'] for run in new_runs]
        classify_start = new_run_numbers[0]
        classify_end = new_run_numbers[-1]

        prompt = f"""# Experiment {experiment_id} - Run Classification (Chunk {chunk_num}/{total_chunks})

{full_content}

# LCLS Run Classification Expert

You are a scientific data analyst specializing in LCLS (Linac Coherent Light Source) experiments. Your task is to analyze logbook entries from experimental runs and classify each run based on its primary purpose and activities.{context_note}

## Classification Framework

Classify each run into exactly ONE of these categories based on its PRIMARY purpose:

### 1. `commissioning_run`
**Definition**: Initial system bring-up, detector setup, and equipment checkout for TMO instruments.

**Key Indicators**:
- MRCO detector commissioning ("ramp up", "checkout", "bias scan")
- MCP gain optimization and tuning
- Spectrometer setup and FZP commissioning
- Beamline transmission checks and KB optics setup
- Initial equipment bring-up without science data collection
- "commission", "checkout", "setup", "bring up" mentions

### 2. `alignment_run`
**Definition**: Spatial positioning of beam, detectors, and optical components.

**Key Indicators**:
- MRCO XY scans and beam centering activities
- Focus positioning and spot size optimization
- TOF detector positioning and angular coverage
- Beam alignment with KB mirrors or other optics
- Spatial overlap procedures (IR/X-ray on paddle)
- "XY scan", "beam center", "focus", "position", "spatial overlap"

### 3. `timing_run`
**Definition**: Temporal synchronization and overlap establishment for pump-probe experiments.

**Key Indicators**:
- ATM timing procedures and t0 determination
- LXT/TXT timing scans and delay stage movements
- Coarse and fine timing optimization
- Temporal overlap establishment (laser/X-ray)
- "timing", "LXT scan", "TXT", "ATM", "t0", "temporal overlap"

### 4. `calibration_run`
**Definition**: Detector calibration, spectral measurements, and system characterization.

**Key Indicators**:
- Retardation voltage scans and optimization
- Photon energy scans for spectral calibration
- FZP spectral reconstruction measurements
- Resolution characterization and detector tuning
- Background measurements and gain calibration
- "retardation scan", "energy scan", "FZP", "spectral", "calibration"

### 5. `measurement_run`
**Definition**: Scientific data collection on samples for research purposes.

**Key Indicators**:
- TMO gas samples: CF4, NNO, Argon, Neon, CO2, N2
- Angular streaking experiments with pump-probe
- Photoelectron spectroscopy data collection
- Scientific measurements with established parameters
- Sample names with measurement context (not just setup)

### 6. `diagnostic_run`
**Definition**: System monitoring, troubleshooting, and performance verification.

**Key Indicators**:
- Signal checking and count rate monitoring
- Transmission monitoring and system verification
- Background measurements and noise characterization
- Equipment status checks and parameter verification
- "signal check", "count rate", "background", "transmission", "status"

### 7. `unknown_run`
**Definition**: Insufficient information to determine the primary purpose despite TMO context.

## Classification Strategy

### TMO Priority Rules
When a run contains multiple activities, classify based on PRIMARY purpose:
1. **Scientific measurement** takes priority over all setup activities
2. **Timing activities** take priority over spatial alignment
3. **Calibration activities** take priority over diagnostic checks
4. **Alignment activities** take priority over commissioning setup
5. **Commissioning** applies only to initial system bring-up phases

### Contextual Analysis and Workflow Logic

Use preceding context runs as an **active validation tool** for all classifications:

**Core Workflow Principles:**
- **Setup → Measurement**: Calibrations/alignments precede data collection
- **Sequential Logic**: Similar runs are often grouped in campaigns
- **Problem Resolution**: Equipment issues trigger test/troubleshooting sequences
- **Session Continuity**: Activities within experimental sessions are logically connected

**For Rich Logbook Entries:**
- **Validate workflow**: Does this classification fit the experimental sequence?
- **Disambiguate**: Use context when entries are ambiguous (e.g., "detector adjustments" after calibration runs → likely `calibration_run`)
- **Verify logic**: Sample runs after troubleshooting may actually be `test_run` to verify fixes

**For Missing/Minimal Entries:**
- **Pattern inference**: 2+ consecutive runs with same classification → likely continuation
- **Sequence logic**: Consider natural progressions (calibration sequences, sample campaigns, alignment procedures)
- **Break point detection**: Don't infer when time gaps, condition changes, or mixed context exist

**Classification Examples:**
- Rich entry + consistent context → `sample_run`, **high confidence**
- "Detector adjustments" + calibration context → `calibration_run`, **medium confidence**
- "No logbook entries" + sample run pattern → `sample_run`, **medium confidence**

### Confidence Guidelines
- **high**: Clear indicators + supportive context + logical workflow
- **medium**: Some clear indicators, minor ambiguity, or pattern-based inference
- **low**: Limited evidence, contradictory activities, or weak context

**Use `unknown_run` only when no discernible pattern exists despite available context.**

## TMO-Specific Domain Knowledge

### TMO Instruments and Equipment:
- **MRCO**: Multi-resolution coincidence detector with 16 TOF spectrometers
- **ATM**: Attosecond timing module for pump-probe experiments
- **XLEAP**: Two-color operation (ω/2ω, fundamental/harmonic modes)
- **FZP**: Fresnel Zone Plate spectrometers for photon diagnostics
- **KB Optics**: Kirkpatrick-Baez focusing mirrors
- **TOF**: Time-of-flight electron spectrometers in angular arrangement

### TMO Sample Types:
- **Gas samples**: CF4 (carbon tetrafluoride), NNO (nitrous oxide), Argon, Neon, CO2, N2
- **Target materials**: SiN windows, YAG screens, GaAs targets
- **Energy range**: 400-1400 eV (soft X-ray regime)

### TMO Measurement Types:
- **Angular streaking**: Time-resolved photoelectron spectroscopy
- **Pump-probe experiments**: IR laser pump, X-ray probe
- **Coincidence spectroscopy**: Correlated electron and photon detection
- **Retardation spectroscopy**: Voltage-tuned electron energy analysis

### TMO Workflow Patterns:
- **Sequential setup**: Commissioning → Alignment → Timing → Calibration → Measurement
- **Pump-probe sequence**: Spatial overlap → Temporal overlap → Science measurements
- **Detector optimization**: Bias tuning → Retardation scans → Count rate optimization

## Required Output (JSON only):

{{
  "experiment_id": "{experiment_id}",
  "chunk_info": {{
    "chunk_number": {chunk_num},
    "total_chunks": {total_chunks},
    "classify_start": {classify_start},
    "classify_end": {classify_end}
  }},
  "classifications": [
    {{
      "run_number": {classify_start},
      "classification": "timing_run",
      "confidence": "high",
      "key_evidence": "LXT timing scan and temporal overlap optimization"
    }}
    // Continue for runs {classify_start} through {classify_end} ONLY
  ]
}}

IMPORTANT: Classify ONLY the NEW runs ({classify_start} through {classify_end}). Do not re-classify context runs. Return ONLY the JSON object with no additional text."""

        return prompt

    def _initialize_output_file(self, output_file: Path, experiment_id: str) -> None:
        """Initialize the output file with metadata"""
        initial_data = {
            "experiment_id": experiment_id,
            "total_runs": 0,
            "processing_info": {
                "processing_mode": "chunked_classification",
                "started_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
                "chunks_completed": 0,
                "token_usage": {
                    "total_tokens": 0,
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "per_chunk_tokens": []
                }
            },
            "classifications": []
        }

        with open(output_file, 'w') as f:
            json.dump(initial_data, f, indent=2)

    def _append_classifications(self, output_file: Path, new_classifications: List[Dict], 
                              chunk_num: int, total_chunks: int, chunk_tokens: int = 0) -> None:
        """Append new classifications to the output file"""
        # Read current data
        with open(output_file, 'r') as f:
            data = json.load(f)

        # Append new classifications
        data["classifications"].extend(new_classifications)
        data["total_runs"] = len(data["classifications"])
        data["processing_info"]["chunks_completed"] = chunk_num
        data["processing_info"]["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

        # Update token usage
        data["processing_info"]["token_usage"]["total_tokens"] = self.total_tokens
        data["processing_info"]["token_usage"]["prompt_tokens"] = self.total_prompt_tokens
        data["processing_info"]["token_usage"]["completion_tokens"] = self.total_completion_tokens
        data["processing_info"]["token_usage"]["per_chunk_tokens"].append(chunk_tokens)

        if chunk_num == total_chunks:
            data["processing_info"]["completed_at"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

        # Write back to file
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

    def _detect_progress_from_output(self, output_file: Path, chunk_size: int) -> int:
        """Detect last completed chunk from existing output file
        
        Args:
            output_file: Path to the output JSON file
            chunk_size: Number of runs per chunk
            
        Returns:
            Next chunk number to start from (1-indexed)
        """
        if not output_file.exists():
            return 1  # Start from beginning
            
        try:
            with open(output_file, 'r') as f:
                data = json.load(f)
            
            classifications = data.get('classifications', [])
            if not classifications:
                return 1
                
            # Find highest run number that's been classified
            max_run = max(c['run_number'] for c in classifications)
            
            # Calculate which chunk contains this run (1-indexed)
            last_completed_chunk = (max_run - 1) // chunk_size + 1
            
            # Start from the next chunk
            next_chunk = last_completed_chunk + 1
            
            self.logger.info(f"Detected progress: highest classified run {max_run} (chunk {last_completed_chunk})")
            return next_chunk
            
        except Exception as e:
            self.logger.warning(f"Could not read output file for progress: {e}")
            return 1

    def classify_runs(self, markdown_content: str, chunk_size: int = 30, 
                     context_runs: int = 5, rate_limit: float = 1.0,
                     output_file: Optional[Path] = None,
                     continue_processing: bool = False) -> Dict[str, Any]:
        """
        Classify runs using chunking with context from preceding runs

        Args:
            markdown_content: Markdown-formatted experiment data
            chunk_size: Number of runs to classify per chunk
            context_runs: Number of preceding runs to include for context
            rate_limit: Delay between API calls in seconds
            output_file: Path for output (automatically detects and resumes from existing progress)
            continue_processing: Continue processing despite chunk failures

        Returns:
            Final classification results dictionary
        """
        # Parse experiment
        experiment_id, total_runs, run_data = self._parse_experiment_file(markdown_content)

        self.logger.info(f"Processing experiment {experiment_id} with {total_runs} runs")
        self.logger.info(f"Chunking: {chunk_size} runs per chunk, {context_runs} preceding runs for context")

        # Calculate chunks
        total_chunks = (total_runs + chunk_size - 1) // chunk_size  # Ceiling division
        self.logger.info(f"Will process {total_chunks} chunks")

        # Initialize output file
        if not output_file:
            output_file = Path(f"{experiment_id}_classifications.json")
        
        # Track failed chunks for fault tolerance
        failed_chunks = []

        # Smart resume from existing output file
        start_chunk = self._detect_progress_from_output(output_file, chunk_size)
        
        if start_chunk > 1:
            self.logger.info(f"Resuming from chunk {start_chunk}/{total_chunks}")
        else:
            self._initialize_output_file(output_file, experiment_id)

        # Process chunks
        print(f"Processing {total_chunks} chunks starting from chunk {start_chunk}", file=sys.stderr)
        for chunk_num in range(start_chunk, total_chunks + 1):
                chunk_start_time = time.time()

                try:
                    # Calculate chunk boundaries
                    run_start_idx = (chunk_num - 1) * chunk_size
                    run_end_idx = min(run_start_idx + chunk_size, total_runs)

                    # Get new runs to classify
                    new_runs = run_data[run_start_idx:run_end_idx]

                    # Get context runs (preceding runs with their classifications)
                    context_content = ""
                    if context_runs > 0 and chunk_num > 1:
                        # Get previous classifications for context
                        previous_classifications = self._read_previous_classifications(output_file, context_runs)

                        # Get corresponding raw run data for context
                        context_start_idx = max(0, run_start_idx - context_runs)
                        context_run_data = run_data[context_start_idx:run_start_idx]

                        context_content = self._create_context_content(previous_classifications, context_run_data)

                    # Create prompt
                    prompt = self._create_prompt(
                        experiment_id, context_content, new_runs, chunk_num, total_chunks
                    )

                    # Make API call
                    self.logger.debug(f"Processing chunk {chunk_num}/{total_chunks}: runs {new_runs[0]['run_number']}-{new_runs[-1]['run_number']}")
                    response, usage = self._make_api_call(prompt)

                    # Track token usage
                    chunk_tokens = usage.get('total_tokens', 0)
                    self.total_tokens += chunk_tokens
                    self.total_prompt_tokens += usage.get('prompt_tokens', 0)
                    self.total_completion_tokens += usage.get('completion_tokens', 0)
                    self.chunk_token_history.append(chunk_tokens)

                    # Extract and validate
                    content = self._validate_response(response)
                    json_content = self._extract_json_from_response(content)
                    result = self._validate_chunk_classifications(json_content)

                    # Append to output
                    self._append_classifications(output_file, result["classifications"], chunk_num, total_chunks, chunk_tokens)


                    # User feedback
                    chunk_time = time.time() - chunk_start_time
                    classified_count = len(result["classifications"])
                    start_run = new_runs[0]['run_number']
                    end_run = new_runs[-1]['run_number']

                    print(f"✓ Chunk {chunk_num}/{total_chunks} complete: classified runs {start_run}-{end_run} ({classified_count} runs, {chunk_tokens:,} tokens) in {chunk_time:.1f}s", file=sys.stderr)

                    # Rate limiting
                    if rate_limit > 0 and chunk_num < total_chunks:
                        time.sleep(rate_limit)

                    # Progress update removed (tqdm dependency removed)

                except Exception as e:
                    self.logger.error(f"Error processing chunk {chunk_num}: {e}")
                    if continue_processing:
                        failed_chunks.append({
                            'chunk': chunk_num,
                            'runs': f"{new_runs[0]['run_number']}-{new_runs[-1]['run_number']}",
                            'error': str(e)
                        })
                        # Progress update removed (tqdm dependency removed)
                        continue
                    else:
                        raise StanfordAPIError(f"Chunk {chunk_num} failed: {e}")

        # Load final result (may be partial if some chunks failed)
        final_result = {}
        if output_file.exists():
            with open(output_file, 'r') as f:
                final_result = json.load(f)
        
        # Report results including failed chunks
        successful_chunks = total_chunks - len(failed_chunks)
        if failed_chunks:
            self.logger.warning(f"Classification partially complete: {successful_chunks}/{total_chunks} chunks succeeded")
            self.logger.warning(f"Failed chunks: {failed_chunks}")
            print(f"\n⚠️  Processing completed with {len(failed_chunks)} failed chunks:", file=sys.stderr)
            for failed in failed_chunks:
                print(f"   • Chunk {failed['chunk']}: runs {failed['runs']} - {failed['error']}", file=sys.stderr)
            
            print(f"\n📊 Results:", file=sys.stderr)
            if final_result:
                classified_runs = len(final_result.get('classifications', {}))
                print(f"   • Successfully classified: {classified_runs} runs", file=sys.stderr)
            print(f"   • Failed chunks: {len(failed_chunks)}", file=sys.stderr)
            
            print(f"\n🔄 To retry failed chunks, run:", file=sys.stderr)
            print(f"   python run_classifier.py [input_file] --resume", file=sys.stderr)
        else:
            self.logger.info(f"Classification complete: {final_result.get('total_runs', 0)} runs classified")
        
        # Add failed chunk info to result for programmatic access
        if final_result:
            final_result['failed_chunks'] = failed_chunks
            final_result['processing_status'] = 'partial' if failed_chunks else 'complete'
            
        return final_result


def setup_logging(verbose: bool = False, debug: bool = False) -> None:
    """Setup logging configuration"""
    level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stderr)
        ]
    )


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description="LCLS Run Classifier with Context-Aware Chunking",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python run_classifier.py experiment.md

  # Custom chunk size and context
  python run_classifier.py experiment.md --chunk-size 20 --context-runs 3

  # Resume processing with fault tolerance
  python run_classifier.py experiment.md --resume

  # With rate limiting and verbose output
  python run_classifier.py experiment.md --rate-limit 2.0 -v

  # Custom settings with fault tolerance
  python run_classifier.py experiment.md --chunk-size 25 --context-runs 5 --resume
        """
    )

    # Required arguments
    parser.add_argument('input_file', type=Path,
                       help='Input markdown file with experiment data')

    # Output options
    parser.add_argument('-o', '--output', type=Path,
                       help='Output JSON file (default: auto-generated from input)')

    # Chunking options
    parser.add_argument('--chunk-size', type=int, default=30,
                       help='Number of runs to classify per chunk (default: 30)')
    parser.add_argument('--context-runs', type=int, default=5,
                       help='Number of preceding runs to include for context (default: 5)')

    # API options
    parser.add_argument('--api-key', 
                       help='Stanford API key (default: STANFORD_API_KEY env var)')
    parser.add_argument('--model', default='claude-3-7-sonnet',
                       help='Model to use (default: claude-3-7-sonnet)')
    parser.add_argument('--rate-limit', type=float, default=1.0,
                       help='Delay between API calls in seconds (default: 1.0)')

    # Fault tolerance options
    parser.add_argument('--resume', action='store_true',
                       help='Resume processing with fault tolerance')
    parser.add_argument('--max-chunk-retries', type=int, default=3,
                       help='Maximum retries per chunk before giving up (default: 3)')

    # Logging options
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--debug', action='store_true',
                       help='Enable debug output')

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.verbose, args.debug)
    logger = logging.getLogger(__name__)

    try:
        # Validate input file
        if not args.input_file.exists():
            logger.error(f"Input file not found: {args.input_file}")
            sys.exit(1)

        # Generate output filename if not provided
        if not args.output:
            base_name = args.input_file.stem
            if base_name.endswith('_enrichment'):
                base_name = base_name[:-11]
            args.output = Path(f"{base_name}_classifications.json")


        # Read input file
        logger.info(f"Reading input file: {args.input_file}")
        with open(args.input_file, 'r') as f:
            markdown_content = f.read()

        # Create classifier
        classifier = RunClassifier(api_key=args.api_key, model=args.model)

        # Process with chunking
        logger.info("Starting classification...")
        result = classifier.classify_runs(
            markdown_content=markdown_content,
            chunk_size=args.chunk_size,
            context_runs=args.context_runs,
            rate_limit=args.rate_limit,
            output_file=args.output,
            continue_processing=args.resume
        )

        print(f"\n✓ Classification complete!", file=sys.stderr)
        print(f"✓ Experiment: {result['experiment_id']}", file=sys.stderr)
        print(f"✓ Total runs: {result['total_runs']}", file=sys.stderr)
        print(f"✓ Chunks processed: {result['processing_info']['chunks_completed']}", file=sys.stderr)
        print(f"✓ Output saved to: {args.output}", file=sys.stderr)

        # Print classification breakdown
        classification_counts = {}
        for classification in result['classifications']:
            cat = classification['classification']
            classification_counts[cat] = classification_counts.get(cat, 0) + 1

        print("✓ Classification breakdown:", file=sys.stderr)
        for cat, count in sorted(classification_counts.items()):
            print(f"  - {cat}: {count}", file=sys.stderr)

        # Token usage summary
        total_chunks = result['processing_info']['chunks_completed']
        avg_tokens = classifier.total_tokens // total_chunks if total_chunks > 0 else 0
        print(f"✓ Token usage: {classifier.total_tokens:,} total (avg {avg_tokens:,} per chunk)", file=sys.stderr)
        print(f"✓ Token breakdown: {classifier.total_prompt_tokens:,} prompt + {classifier.total_completion_tokens:,} completion", file=sys.stderr)

    except KeyboardInterrupt:
        logger.info("Processing interrupted by user")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
