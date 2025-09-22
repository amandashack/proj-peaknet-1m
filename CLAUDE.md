# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development Commands
```bash
# Run single experiment classification
python run_classifier.py processed_experiments/mfx101080524_enrichment.md

# Batch processing from CSV
python batch_run_classifier.py crystallography.csv

# Preprocess logbook data (single experiment)
python preprocess_logbook.py --experiment mfxl1027922 --output processed_data.md

# Bulk preprocessing with parallel processing
python batch_preprocess_logbook.py

# Fill enrichment placeholders
python batch_fill_enrichment.py

# Analyze token usage and costs
python token_summary.py

# Analyze experiment documentation quality
python analyze_empty_run_ratios.py on_disk_2025_0820_preprocessed_experiments/*.md -o empty_run_analysis.csv
```

### Environment Setup
```bash
# Set Stanford API key (required for classification)
export STANFORD_API_KEY="your_api_key_here"
```

### Quality Filtering Commands
```bash
# Filter out poorly documented experiments (>80% empty runs)
awk -F',' 'NR==1 || $4 < 0.8' empty_run_analysis.csv > usable_experiments.csv

# Keep only high-quality experiments (<50% empty)
awk -F',' 'NR==1 || $4 < 0.5' empty_run_analysis.csv > high_quality_experiments.csv

# Get quality statistics
echo "Total: $(tail -n +2 empty_run_analysis.csv | wc -l)"
echo "Usable (<80%): $(awk -F',' 'NR>1 && $4 < 0.8' empty_run_analysis.csv | wc -l)"
```

## Architecture

### Core Pipeline
```
SQLite Database (logbook entries)
         ↓
   preprocess_logbook.py (batch_preprocess_logbook.py for bulk)
         ↓
*_enrichment.md (with __ANSWER__ placeholders)
         ↓
   run_classifier.py (batch_run_classifier.py for bulk)
         ↓
*_classifications.json
         ↓
   fill_enrichment.py (batch_fill_enrichment.py for bulk)
         ↓
*_full_enrichment.md (complete)
```

### Key Components

**RunClassifier class** (`run_classifier.py:30-36`):
- Context-aware chunking system that builds classifications incrementally
- Each chunk includes preceding runs with their classifications as context
- Uses Stanford AI Gateway API with robust retry mechanisms
- Tracks token usage across chunks for cost analysis

**LogbookPreprocessor class** (`preprocess_logbook.py:22-50`):
- Extracts and groups logbook entries by run number from SQLite database
- Cleans HTML content and formats data for LLM processing
- Supports filtering patterns for content refinement

**BatchProcessor class** (`batch_preprocess_logbook.py:106`):
- Parallel processing of multiple experiments
- Resume functionality for interrupted batch jobs
- Handles large-scale preprocessing operations

### Classification Categories

#### Original LCLS Categories (Generic)
- `sample_run`: Data collection on actual samples
- `calibration_run`: Instrument calibration and setup
- `alignment_run`: Beam/instrument alignment procedures
- `test_run`: Equipment testing and validation
- `commissioning_run`: Initial system commissioning
- `unknown_run`: Unclear or insufficient information

#### TMO-Specific Categories (Current)
- `measurement_run`: Scientific data collection on samples
- `calibration_run`: Instrument calibration and baseline establishment
- `alignment_run`: Spatial beam/instrument alignment
- `timing_run`: Temporal alignment and synchronization
- `commissioning_run`: Initial system setup and commissioning
- `diagnostic_run`: System testing and troubleshooting
- `unknown_run`: Insufficient information for classification

### Data Flow

1. **Preprocessing**: Extract logbook entries from SQLite database, group by runs, clean HTML
2. **Classification**: Use context-aware chunking to classify runs via Stanford AI API
3. **Enrichment**: Fill placeholder templates with classification results
4. **Quality Analysis**: Analyze documentation quality to filter experiments worth processing

### File Structure

- `*.py`: Core pipeline scripts (preprocessing, classification, enrichment)
- `batch_*.py`: Bulk processing variants with parallel execution
- `crystallography.csv`: Experiment list for batch processing
- `processed_experiments/`: Preprocessed markdown files with placeholders
- `*_classifications.json`: Classification results from AI processing
- `*_full_enrichment.md`: Final enriched documents

### Configuration

- **Stanford API Key**: Required environment variable `STANFORD_API_KEY`
- **Model**: Default is `claude-3-7-sonnet` (configurable)
- **Token Limits**: 8192 max tokens per API call
- **Temperature**: 0.1 for consistent classifications
- **Retry Strategy**: 3 attempts with exponential backoff for API calls

### Quality Filtering Strategy

The pipeline includes sophisticated quality analysis to optimize API costs and classification accuracy:
- **High Quality (<50% empty)**: ~92 experiments with rich documentation
- **Usable (50-80% empty)**: ~14 experiments with mixed quality
- **Garbage (>80% empty)**: ~18 experiments with minimal content (filter out)

Filtering saves ~15% of API costs by excluding experiments that produce poor results.

## TMO-Specific Implementation

### TMO Instrument Focus
This pipeline has been optimized for **TMO (Time-resolved Molecular and Optical Science)** experiments at LCLS. TMO specializes in:

- **Pump-probe experiments**: IR laser pump, X-ray probe timing studies
- **Photoelectron spectroscopy**: Angular-resolved electron detection
- **Coincidence measurements**: Correlated electron and photon detection
- **Attosecond timing**: Ultra-precise temporal alignment capabilities

### TMO Equipment and Workflow
- **MRCO**: Multi-resolution coincidence detector with 16 TOF spectrometers
- **ATM**: Attosecond timing module for precise pump-probe synchronization
- **FZP**: Fresnel Zone Plate spectrometers for photon diagnostics
- **Retardation spectroscopy**: Voltage-tuned electron energy analysis

### Classification Evolution

#### Version History
- **Original**: Generic LCLS categories (6 categories)
- **TMO v1**: TMO-specific categories with 79% validation accuracy
- **TMO v2**: Enhanced prompt with contextual rules and priority logic

#### TMO v2 Improvements
- **Priority keyword system**: High-priority terms override ambiguous context
- **Contextual pattern rules**: Run number, duration, and sequence analysis
- **Technical issue handling**: Classify by intended purpose, not outcome
- **Special TMO cases**: Interleaved retardation mode, gas injection patterns

### Performance Benchmarks
- **TMO v1 Baseline**: 79% accuracy (298/377 correct, 79 corrections needed)
- **TMO v2 Target**: 85-90% accuracy through improved disambiguation
- **Key improvements**: Reduced `unknown_run` overuse, better measurement/calibration distinction

### Validation Workflow
Use the validation app at `/sdf/scratch/users/a/ajshack/dev/run-classification-validation-app/` for manual verification and accuracy measurement.