# LCLS Run Classification Pipeline

AI-powered classification of LCLS experimental runs from logbook entries.

## 🔄 Core Pipeline

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

## 📋 Core Scripts

**Data Preprocessing:**
- `preprocess_logbook.py` - Extract logbook entries from SQLite database
- `batch_preprocess_logbook.py` - Bulk preprocessing with parallel processing

**Classification:**
- `run_classifier.py` - Classify runs using AI (6 categories: sample, calibration, alignment, test, commissioning, unknown)
- `batch_run_classifier.py` - Process multiple experiments from CSV

**Enrichment:**
- `fill_enrichment.py` - Fill __ANSWER__ placeholders with classifications
- `batch_fill_enrichment.py` - Bulk placeholder filling

**Analysis:**
- `token_summary.py` - Analyze token usage and costs
- `analyze_empty_run_ratios.py` - Analyze documentation quality (empty run ratios) of preprocessed experiments

## 🚀 Quick Start

```bash
# Single experiment
python run_classifier.py processed_experiments/mfx101080524_enrichment.md

# Batch processing  
python batch_run_classifier.py crystallography.csv

# Fill placeholders
python batch_fill_enrichment.py
```

## 📊 Experiment Quality Filtering

Filter out poorly documented experiments to improve classification quality and reduce API costs.

### 🔍 Analyze Documentation Quality

```bash
# Generate quality analysis from preprocessed experiments
python analyze_empty_run_ratios.py on_disk_2025_0820_preprocessed_experiments/*.md -o empty_run_analysis.csv
```

### ⚡ Filter Using Unix Commands

```bash
# Remove poorly documented experiments (>80% empty runs) 
awk -F',' 'NR==1 || $4 < 0.8' empty_run_analysis.csv > usable_experiments.csv

# Extract only garbage experiments (>=80% empty)
awk -F',' 'NR==1 || $4 >= 0.8' empty_run_analysis.csv > garbage_experiments.csv  

# Keep only high-quality experiments (<50% empty)
awk -F',' 'NR==1 || $4 < 0.5' empty_run_analysis.csv > high_quality_experiments.csv
```

### 📈 Quality Statistics

```bash
echo "Total: $(tail -n +2 empty_run_analysis.csv | wc -l)"
echo "Usable (<80%): $(awk -F',' 'NR>1 && $4 < 0.8' empty_run_analysis.csv | wc -l)"  
echo "Garbage (>=80%): $(awk -F',' 'NR>1 && $4 >= 0.8' empty_run_analysis.csv | wc -l)"
```

### 💡 Quality Tiers

- **High Quality (<50% empty)**: ~92 experiments - Rich documentation, reliable classifications
- **Usable (50-80% empty)**: ~14 experiments - Mixed quality, worth processing  
- **Garbage (>80% empty)**: ~18 experiments - Minimal content, poor ROI - **filter out**

### 🔧 Practical Usage

```bash
# Use filtered list with batch processing
python batch_run_classifier.py usable_experiments.csv
```

**Benefits**: Saves ~15% of API costs by filtering out experiments that produce poor classification results.