# TMO Prompt V2 Instructions

## Validation Analysis Summary
Based on validation of 377 runs from experiment tmox1016823:
- **Accuracy**: 79.0% (79 corrections needed)
- **Major Issues**:
  1. Measurement vs Calibration confusion (32 corrections)
  2. Overuse of Unknown classification (30 corrections)
  3. Commissioning vs Test confusion (4 corrections)

## Key Improvements for V2

### 1. Clarify Measurement vs Calibration Distinction

#### `calibration_run` - Enhanced Definition
**Definition**: System calibration, baseline measurements, and parameter optimization WITHOUT scientific data collection intent.

**Updated Key Indicators**:
```
STRONG INDICATORS:
- "baseline scan" or "baseline measurement"
- "test scan" or "test of scanning"
- "parameter optimization" or "tuning"
- HV settings, gain adjustments, bias scans
- Argon/Neon used for calibration (not data collection)
- Retardation/energy scans for system optimization

NEGATIVE INDICATORS (NOT calibration):
- Explicit data collection for analysis
- Scientific measurements with publication intent
```

#### `measurement_run` - Enhanced Definition
**Definition**: Scientific data collection with clear intent to analyze results for research purposes.

**Updated Key Indicators**:
```
STRONG INDICATORS:
- "collecting data", "recording", "measuring for analysis"
- Sample measurements WITH analysis intent
- Explicit mention of scientific goals
- Data quality assessments ("good hits", "nice signal")

NEGATIVE INDICATORS (NOT measurement):
- "no data collected" or "no data"
- "test scan" or "baseline"
- "parking position" for needle
- Just "injected Argon" without collection intent
```

### 2. Handle Technical Issues and Crashes

#### New Decision Rule
```
When technical issues occur (crashes, PMPS failures, aborted runs):
1. Identify the INTENDED purpose before the issue
2. Classify based on INTENT, not outcome
3. Look for keywords indicating what was being attempted
4. Only use unknown_run if intent is completely unclear

Examples:
- "PMPS crashed during Argon measurement" → measurement_run (intent clear)
- "System crashed, no data" with retardation scan → calibration_run
- "Keep crashing" during alignment → alignment_run
```

### 3. Refine Test vs Commissioning Distinction

#### `commissioning_run` - Narrowed Definition
**Definition**: INITIAL system bring-up and first-time setup ONLY (typically runs 1-10).

**Updated Indicators**:
```
- First runs of experiment (runs 1-10 typical)
- "initial setup", "first time", "bring-up"
- "checkout" in early runs
- Detector first-time configuration
```

#### `test_run` - Expanded Definition
**Definition**: Testing and verification AFTER initial commissioning phase.

**Updated Indicators**:
```
- "test run" explicit mention
- "test of" any system/procedure
- Verification of existing setup
- Runs after initial commissioning (>run 10)
- System verification without data collection
```

### 4. Priority Keyword System

#### HIGH PRIORITY Keywords (Override Other Indicators)
```python
keyword_priorities = {
    "baseline scan": "calibration_run",
    "baseline measurement": "calibration_run",
    "test run": "test_run",
    "test of scanning": "calibration_run",
    "collecting data for": "measurement_run",
    "data collection": "measurement_run",
    "no data": "NOT measurement_run",  # Negative indicator
    "parking position": "NOT measurement_run",  # Negative indicator
}
```

#### Classification Priority Order
1. Check HIGH PRIORITY keywords first
2. Check NEGATIVE indicators to rule out classifications
3. Apply standard classification logic
4. Consider context (run number, duration, surrounding runs)

### 5. Contextual Pattern Rules

#### Run Number Context
```
Runs 1-5: Higher probability of commissioning/test
Runs 6-20: Likely alignment/calibration setup
Runs 20+: Mixed activities, rely on content
Very late runs (>300): Often cleanup/verification
```

#### Duration Context
```
<30 seconds: Check for abort/crash, classify by intent
30s-2min: Typical calibration/alignment
2-10min: Typical measurement or complex calibration
>1 hour: Check for issues, often crashed measurement attempts
```

#### Sequential Context
```
If previous 2+ runs are calibration → likely calibration
If following known measurement → likely measurement continuation
Alternating patterns → check retardation changes (interleaved mode)
```

### 6. Special TMO Cases

#### Interleaved Retardation Mode
```
When "interleaved retardation" mentioned:
- Multiple TOFs at different voltages = usually calibration
- Unless explicit "data collection" mentioned
- Pattern: 0°, 90°, 180°, 270° at different V
```

#### Gas Injection Without Collection
```
"Argon injected" alone → check for:
- "parking position" → NOT measurement
- "baseline" → calibration
- "collecting" → measurement
- No other keywords → calibration
```

#### FZP Spectrometer Settings
```
FZP settings changes:
- During runs 1-50 → likely calibration
- With "spectral reconstruction" → calibration
- With sample data collection → measurement
```

## Implementation Checklist

- [ ] Update calibration_run definition with baseline/test scan keywords
- [ ] Update measurement_run with positive data collection indicators
- [ ] Add negative indicator checks before classification
- [ ] Implement technical issue handling rules
- [ ] Narrow commissioning_run to runs 1-10 typically
- [ ] Expand test_run definition
- [ ] Add priority keyword checking
- [ ] Implement contextual patterns (run number, duration, sequence)
- [ ] Add special TMO equipment pattern recognition
- [ ] Update confidence scoring based on keyword matches

## Expected Improvements

With these changes, we expect:
- **Measurement/Calibration accuracy**: 90%+ (from current 70%)
- **Unknown classification reduction**: 50% fewer unknowns
- **Overall accuracy**: 85-90% (from current 79%)
- **Better handling of**: Technical issues, aborted runs, commissioning phase

## Testing Strategy

1. Re-run classification on tmox1016823 with V2 prompt
2. Compare against validated results
3. Focus analysis on previously misclassified runs:
   - Runs 21, 122, 228-231 (measurement→calibration)
   - Runs 18, 100-105 (→unknown)
   - Runs 1-4 (commissioning→test)
4. Iterate if patterns remain

## Notes for Implementation

- Keep all existing TMO equipment recognition (MRCO, ATM, etc.)
- Maintain hierarchical structure but refine decision boundaries
- Add examples from actual misclassified runs
- Consider adding a "confidence boost" for keyword matches
- Log which rules triggered for each classification (for debugging)