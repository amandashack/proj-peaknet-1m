# LCLS vs TMO Classification System Comparison

## Executive Summary
Transformation from generic LCLS classification to TMO-specific system with specialized categories, equipment recognition, and workflow awareness.

---

## 📊 Classification Categories Comparison

### Original LCLS System (6 categories)
```
1. sample_run       - Any sample measurement
2. calibration_run  - Detector calibration, DARK
3. alignment_run    - Beam alignment, positioning
4. test_run         - Equipment testing
5. commissioning_run - Initial setup
6. unknown_run      - Insufficient information
```

### TMO-Specific System (7 categories)
```
1. commissioning_run - MRCO detector setup, MCP tuning, system bring-up
2. alignment_run     - MRCO XY scans, beam centering, focus optimization
3. timing_run        - ATM timing, LXT/TXT scans, temporal overlap [NEW]
4. calibration_run   - Retardation scans, energy scans, FZP calibration
5. measurement_run   - CF4/NNO/Argon data, angular streaking [RENAMED from sample_run]
6. diagnostic_run    - Signal checks, count rates, monitoring [RENAMED from test_run]
7. unknown_run       - Insufficient TMO context
```

### Key Changes:
- **Added**: `timing_run` - Critical for TMO pump-probe experiments
- **Renamed**: `sample_run` → `measurement_run` (TMO-specific terminology)
- **Renamed**: `test_run` → `diagnostic_run` (better reflects TMO usage)
- **Enhanced**: All categories now have TMO-specific indicators

---

## 🔧 Equipment Recognition

### Original LCLS Context
```
Generic Equipment:
- Detectors, motors, mirrors, injectors
- YAG screens
- General LCLS instruments (AMO, CXI, MFX, MEC, XPP, XCS)
- No specific equipment patterns
```

### TMO-Specific Context
```
TMO Equipment Hierarchy:
├── MRCO (Multi-resolution coincidence detector)
│   ├── 16 TOF spectrometers
│   ├── MCP detectors with bias tuning
│   └── Retardation voltage systems (0-500V)
├── ATM (Attosecond timing module)
│   ├── LXT/TXT delay stages
│   └── Pump-probe synchronization
├── XLEAP Operation
│   ├── ω/2ω two-color mode
│   └── 350/700 eV harmonic generation
├── FZP Spectrometers
│   └── Zone plates: 400, 530, 613, 690, 950 eV
└── KB Optics (focusing mirrors)
```

---

## 🧪 Sample Recognition

### Original LCLS Context
```
Generic Samples:
- "Proteins, crystals, foils, gases, liquids"
- Chemical formulas (e.g., "Fe(bpy)3", "10mM protein")
- No instrument-specific patterns
```

### TMO-Specific Context
```
TMO Gas Samples (with context):
├── CF4 (Carbon tetrafluoride)
│   ├── F-edge: 690 eV resonance
│   └── C-edge: Angular streaking
├── NNO (N2O - Nitrous oxide)
│   ├── N-edge: 410 eV
│   └── O-edge: 530 eV
├── Argon
│   └── L-edge: 400 eV calibration
├── Neon, CO2, N2
└── Target materials: SiN, YAG, GaAs

Energy Ranges:
- Soft X-ray: 400-1400 eV
- Common working points: 400, 690, 750, 950 eV
```

---

## 🔄 Workflow Recognition

### Original LCLS Context
```
Simple Priority Rules:
1. Sample measurement > setup activities
2. Calibration > routine maintenance
3. Alignment > general testing
4. Commissioning for dedicated runs only
```

### TMO-Specific Context
```
TMO Workflow Sequences:
┌─────────────────┐
│ Commissioning   │ → Initial bring-up, MCP bias scans
└────────┬────────┘
         ↓
┌─────────────────┐
│   Alignment     │ → MRCO XY scans, beam centering
└────────┬────────┘
         ↓
┌─────────────────┐
│    Timing       │ → LXT/TXT scans, t0 determination
└────────┬────────┘
         ↓
┌─────────────────┐
│  Calibration    │ → Retardation/energy scans
└────────┬────────┘
         ↓
┌─────────────────┐
│  Measurement    │ → Scientific data collection
└─────────────────┘

Sub-workflows:
- Pump-probe: Spatial overlap → Temporal overlap → Measurement
- Detector optimization: Bias tuning → Retardation → Count rate
```

---

## 📝 Key Indicator Patterns

### Original LCLS Indicators
| Category | Generic Indicators |
|----------|-------------------|
| sample_run | "sample", "injection", "data collection" |
| calibration_run | "DARK", "pedestal", "gain" |
| alignment_run | "beam alignment", "mirror" |
| test_run | "testing", "troubleshooting" |

### TMO-Specific Indicators
| Category | TMO-Specific Indicators |
|----------|------------------------|
| commissioning_run | "MRCO ramp up", "bias scan", "MCP gain", "checkout" |
| alignment_run | "MRCO XY scan", "beam center", "TOF positioning" |
| timing_run | "LXT scan", "TXT", "ATM timing", "t0", "temporal overlap" |
| calibration_run | "retardation scan", "energy scan", "FZP", "interleaved mode" |
| measurement_run | "CF4", "NNO", "angular streaking", "pump-probe data" |
| diagnostic_run | "signal check", "count rate", ">1000 Hz", "transmission" |

---

## 📈 Performance Metrics (To Be Filled After Validation)

### Classification Accuracy
```
┌─────────────────────────────────────────────────┐
│                                                 │
│  Original LCLS System:                         │
│  ├── Overall Accuracy: [ TBD ]%                │
│  ├── Confidence Distribution:                  │
│  │   ├── High: [ TBD ]%                       │
│  │   ├── Medium: [ TBD ]%                     │
│  │   └── Low: [ TBD ]%                        │
│  └── Unknown Classifications: [ TBD ]%         │
│                                                 │
│  TMO-Specific System:                          │
│  ├── Overall Accuracy: [ TBD ]%                │
│  ├── Confidence Distribution:                  │
│  │   ├── High: [ TBD ]%                       │
│  │   ├── Medium: [ TBD ]%                     │
│  │   └── Low: [ TBD ]%                        │
│  └── Unknown Classifications: [ TBD ]%         │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Per-Category Performance
```
Category               | Original | TMO-Specific | Improvement
-----------------------|----------|--------------|------------
commissioning_run      | [ TBD ]% | [ TBD ]%     | [ +/- ]%
alignment_run          | [ TBD ]% | [ TBD ]%     | [ +/- ]%
timing_run             | N/A      | [ TBD ]%     | NEW
calibration_run        | [ TBD ]% | [ TBD ]%     | [ +/- ]%
measurement/sample_run | [ TBD ]% | [ TBD ]%     | [ +/- ]%
diagnostic/test_run    | [ TBD ]% | [ TBD ]%     | [ +/- ]%
unknown_run            | [ TBD ]% | [ TBD ]%     | [ +/- ]%
```

### Validation Insights
```
┌─────────────────────────────────────────────────┐
│ Experiment: tmol1034523 (123 runs)             │
│ ├── Manual Corrections Required: [ TBD ]       │
│ ├── Most Confused Categories: [ TBD ]          │
│ └── Time to Validate: [ TBD ]                  │
│                                                 │
│ Experiment: tmox1016823 (377 runs)             │
│ ├── Manual Corrections Required: [ TBD ]       │
│ ├── Most Confused Categories: [ TBD ]          │
│ └── Time to Validate: [ TBD ]                  │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Key Improvements

### 1. **Domain Specificity**
- From generic LCLS → TMO-specific terminology
- Recognition of TMO equipment patterns
- Understanding of TMO experimental workflows

### 2. **Workflow Intelligence**
- Sequential dependency recognition
- Sub-workflow patterns (pump-probe, detector optimization)
- Context-aware classification based on experimental phase

### 3. **Enhanced Granularity**
- New `timing_run` category for critical TMO operations
- Distinction between `measurement` (science) and `diagnostic` (monitoring)
- TMO-specific evidence patterns

### 4. **Equipment Context**
- MRCO detector system understanding
- ATM timing module recognition
- Retardation voltage and energy scan patterns

---

## 💡 Expected Benefits

1. **Higher Accuracy**: TMO-specific patterns reduce misclassification
2. **Better Granularity**: 7 categories vs 6, with timing separated
3. **Reduced Unknown**: TMO context helps classify ambiguous runs
4. **Workflow Alignment**: Categories match actual TMO operational phases
5. **Faster Validation**: Better initial classifications require fewer corrections

---

## 📋 Notes for Validation

When validating, pay special attention to:
- Runs previously classified as `calibration_run` that might be `timing_run`
- `test_run` vs `diagnostic_run` distinction
- `sample_run` vs `measurement_run` terminology
- Commissioning activities at experiment start
- Sequential workflow patterns (commissioning → alignment → timing → calibration → measurement)

---

*Document generated: 2025-09-17*
*TMO Experiments: tmol1034523 (123 runs), tmox1016823 (377 runs)*
*Total runs classified: 500*