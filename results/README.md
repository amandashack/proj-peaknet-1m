# TMO Classification Results Comparison

## Directory Structure

### `original/`
Results from the original LCLS prompt (before TMO modifications)
- Uses standard categories: sample_run, test_run, calibration_run, alignment_run, commissioning_run, unknown_run

### `tmo_v1/`  
Results from TMO Prompt v1 (initial TMO-specific categories)
- New categories: commissioning_run, alignment_run, timing_run, calibration_run, measurement_run, diagnostic_run, unknown_run
- **Validation accuracy**: 79% on tmox1016823 (79/377 corrections needed)
- **Key improvements**: TMO equipment recognition, timing activities, measurement context

### `tmo_v2/`
Results from TMO Prompt v2 (refined based on validation feedback) 
- Same categories as v1 but improved decision logic
- **Expected accuracy**: 85-90%
- **Key improvements**: Better measurement/calibration distinction, technical issue handling

## File Types

- `classifications/`: Raw classification JSON outputs from run_classifier.py
- `validations/`: Manual validation results from rcv tool  
- `enrichments/`: Full enrichment markdown files with classifications filled in
- `TMO_Performance_Comparison_*.md`: Analysis documents

## Experiments

- **tmox1016823**: MRCO Commissioning experiment (377 runs) - fully validated
- **tmol1034523**: L1034523 experiment (123 runs) - partially validated

## Usage

```bash
# Compare classification outputs
diff results/original/classifications/tmox1016823_classifications.json \
     results/tmo_v1/classifications/tmox1016823_classifications.json

# Analyze validation results  
python3 analyze_validation_results.py results/tmo_v1/validations/
```
