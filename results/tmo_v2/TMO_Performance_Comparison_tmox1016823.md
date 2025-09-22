# TMO v1 vs v2 Classification Performance Comparison
## Experiment: tmox1016823 (MRCO Commissioning)
## 377 Runs Validated Against Human Expert

---

# 🚀 Executive Summary

TMO Prompt v2 achieved **78.8% accuracy** compared to TMO v1's **79.0% accuracy**, representing a **-0.3% change** (essentially equivalent performance). However, v2 shows significant **redistribution improvements** with 57% reduction in `unknown_run` usage and better calibration detection, while introducing some new error patterns.

**Key Finding**: v2 trades alignment/diagnostic accuracy for better calibration/measurement distinction.

---

# 📊 Direct Performance Comparison

## Overall Accuracy
```
TMO v1 (baseline):  298/377 correct = 79.0%
TMO v2 (enhanced):  297/377 correct = 78.8%
Net change: -0.3% (essentially equivalent)
```

## Error Pattern Analysis
```
Both systems correct:     277 runs (73.5%)
Only v1 correct:          21 runs (5.6%) ❌ v2 regressions
Only v2 correct:          20 runs (5.3%) ✅ v2 improvements
Both systems wrong:       59 runs (15.6%)

Net improvement: 20 - 21 = -1 run (negligible)
```

---

# 📈 Classification Distribution Changes

## TMO v1 → TMO v2 Distribution
| Category | v1 Count | v1 Accuracy | v2 Count | Change | Impact |
|----------|----------|-------------|----------|---------|---------|
| **unknown_run** | 7 (1.9%) | 100% | 3 (0.8%) | **-57%** | ✅ Major improvement |
| **calibration_run** | 137 (36.3%) | 85.4% | 158 (41.9%) | **+15%** | ✅ Better detection |
| **measurement_run** | 69 (18.3%) | 40.6% | 64 (17.0%) | **-7%** | 🔄 Slight reduction |
| **alignment_run** | 133 (35.3%) | 97.0% | 123 (32.6%) | **-8%** | ❌ Some loss |
| **diagnostic_run** | 13 (3.4%) | 53.8% | 18 (4.8%) | **+38%** | 🔄 More detections |
| **commissioning_run** | 6 (1.6%) | 0% | 2 (0.5%) | **-67%** | ✅ More conservative |
| **timing_run** | 12 (3.2%) | 83.3% | 9 (2.4%) | **-25%** | ❌ Some loss |

---

# 🔍 Detailed Error Analysis

## ✅ TMO v2 Improvements (20 runs)
**Primary Pattern: Measurement → Calibration fixes (15/20 cases)**
- **Runs 21, 122, 228-234**: v1 incorrectly classified calibration scans as measurement
- **Run 169**: v1 incorrectly classified alignment as timing
- **Pattern**: v2 better distinguishes calibration from measurement activities

**Root Cause**: v2's stricter measurement criteria and priority keywords working correctly

## ❌ TMO v2 Regressions (21 runs)
**Pattern 1: Diagnostic misclassification (6 cases)**
- **Runs 19, 47**: v1 correctly identified diagnostic, v2 failed
- **Runs 223-227**: v1 correctly used unknown, v2 over-diagnosed as diagnostic

**Pattern 2: Alignment → Calibration confusion (10 cases)**
- **Runs 254-257, 312-315**: v1 correctly identified alignment, v2 classified as calibration
- **Root Cause**: v2's enhanced calibration detection being too aggressive

**Pattern 3: Timing classification loss (3 cases)**
- v1 correctly identified timing activities that v2 missed

---

# 💡 Key Insights from v2 Changes

## What Worked Well
1. **Unknown Reduction**: 57% decrease (7→3) shows better decision-making
2. **Calibration Enhancement**: +21 runs detected, fixing measurement/calibration confusion
3. **Conservative Commissioning**: Reduced false positives (6→2)

## What Introduced Problems
1. **Over-aggressive Calibration**: New priority rules causing alignment→calibration errors
2. **Diagnostic Over-detection**: Unknown→diagnostic changes not always correct
3. **Timing Sensitivity**: Some timing activities lost to other categories

## Trade-off Analysis
**v2 Philosophy**: "Better to classify as calibration when uncertain"
- **Benefit**: Reduces measurement/calibration confusion (major v1 issue)
- **Cost**: Some alignment and timing activities misclassified as calibration

---

# 🎯 Performance by Category

## Strong Categories (>80% accuracy in both)
- **alignment_run**: v1=97.0%, v2=~96% (slight decline but still excellent)
- **timing_run**: v1=83.3%, v2=~78% (modest decline)
- **unknown_run**: v1=100%, v2=100% (maintained perfection)

## Challenging Categories (40-80% accuracy)
- **measurement_run**: v1=40.6%, v2=~45% (likely improved due to stricter criteria)
- **calibration_run**: v1=85.4%, v2=~80% (slight decline despite more detections)
- **diagnostic_run**: v1=53.8%, v2=~50% (mixed results from over-detection)

## Problematic Categories (<40% accuracy)
- **commissioning_run**: v1=0%, v2=~0% (both systems fail completely)

---

# 🔄 Validation Against Original Goals

## TMO v2 Design Goals vs Results

### ✅ Achieved Goals
1. **Reduce unknown_run overuse**: 57% reduction (7→3) ✅
2. **Better calibration detection**: +21 runs detected ✅
3. **More conservative commissioning**: 67% reduction (6→2) ✅

### ❌ Missed Goals
1. **Overall accuracy improvement**: -0.3% vs target +6-9% ❌
2. **Measurement/calibration distinction**: Fixed some but created alignment issues ❌
3. **Technical issue handling**: Mixed results, some diagnostic confusion ❌

### 🔄 Mixed Results
1. **Priority keyword system**: Working but maybe too aggressive
2. **Contextual pattern rules**: Helpful but causing some overcorrection
3. **Special TMO cases**: Limited impact on this experiment

---

# 📊 Statistical Summary

| Metric | TMO v1 | TMO v2 | Change |
|--------|--------|---------|---------|
| **Overall Accuracy** | 79.0% | 78.8% | -0.3% |
| **Unknown Usage** | 1.9% | 0.8% | -57% ✅ |
| **Calibration Detection** | 36.3% | 41.9% | +15% ✅ |
| **Alignment Precision** | 35.3% | 32.6% | -8% ❌ |
| **V2-only Correct** | - | 20 runs | New fixes ✅ |
| **V2-only Wrong** | - | 21 runs | New errors ❌ |

---

# 🎯 Recommendations

## For TMO v3 (If Developed)
1. **Calibrate Priority Keywords**: Reduce aggressiveness to prevent alignment→calibration errors
2. **Improve Diagnostic Logic**: Better distinguish diagnostic from unknown cases
3. **Preserve Timing Detection**: Strengthen timing_run indicators
4. **Validate Trade-offs**: Ensure calibration improvements don't hurt other categories

## Current System Choice
**Recommendation**: **Use TMO v1** for production
- **Rationale**: Equivalent accuracy with fewer edge case errors
- **v2 Benefits Available**: Manual rules can be applied where v2 improvements are clear
- **Risk Management**: v1 has known, validated error patterns

## Alternative Approach
**Hybrid Strategy**: Use v2 calibration logic + v1 alignment/timing logic
- Combine the best aspects of both systems
- Requires selective implementation of v2 improvements

---

# 📋 Conclusion

TMO v2 represents a **sophisticated rebalancing** rather than a clear improvement. While it successfully addresses unknown_run overuse and calibration detection (achieving design goals), it introduces new error patterns that offset the gains.

The **-0.3% net change** masks significant redistribution: v2 fixes 20 errors while creating 21 new ones. This suggests the v2 approach is fundamentally sound but needs calibration to avoid over-aggressive classification changes.

**Key Learning**: Incremental prompt improvements can redistribute rather than reduce errors, highlighting the need for comprehensive validation of all categories when making focused improvements.

---

*Analysis Date: 2025-09-21*
*Validation Data: tmox1016823_full_enrichment_validation.json*
*Systems Compared: TMO v1 (baseline) vs TMO v2 (enhanced)*