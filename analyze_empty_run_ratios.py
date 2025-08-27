#!/usr/bin/env python3
"""
Empty Run Ratio Analysis Utility

Analyzes preprocessed LCLS experiment files to determine the ratio of 
runs with no logbook entries vs total runs. Helps identify experiments
that would waste LLM tokens due to lack of meaningful content.

Usage:
    python analyze_empty_run_ratios.py experiment1.md experiment2.md
    python analyze_empty_run_ratios.py experiments/*.md -o results.csv
    python analyze_empty_run_ratios.py experiments/*.md -q

Output:
    CSV file with columns: experiment_id,total_runs,empty_runs,empty_ratio
"""

import argparse
import subprocess
import csv
import os
from pathlib import Path


def count_pattern_in_file(filepath, pattern):
    """Count occurrences of a pattern in a file using grep"""
    try:
        result = subprocess.run(['grep', '-c', pattern, filepath], 
                              capture_output=True, text=True)
        return int(result.stdout.strip()) if result.returncode == 0 else 0
    except:
        return 0


def analyze_experiment_file(filepath):
    """Analyze a single experiment file and return metrics"""
    # Extract experiment ID from filename
    filename = Path(filepath).name
    if filename.endswith('_enrichment.md'):
        suffix_start = filename.rfind('_enrichment.md')
        exp_id = filename[:suffix_start]
    else:
        exp_id = Path(filepath).stem

    # Count total runs and empty runs
    total_runs = count_pattern_in_file(filepath, '^### Run')
    empty_runs = count_pattern_in_file(filepath, 'No logbook entries')

    # Calculate ratio
    ratio = empty_runs / total_runs if total_runs > 0 else 0

    return {
        'experiment_id': exp_id,
        'total_runs': total_runs,
        'empty_runs': empty_runs,
        'empty_ratio': round(ratio, 3)
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze empty run ratios in LCLS experiment files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze_empty_run_ratios.py experiment.md
  python analyze_empty_run_ratios.py exp1.md exp2.md exp3.md
  python analyze_empty_run_ratios.py experiments/*.md
  python analyze_empty_run_ratios.py experiments/*.md -o results.csv
  python analyze_empty_run_ratios.py experiments/*.md -q
        """
    )
    
    parser.add_argument('files', nargs='+', 
                       help='One or more experiment files to analyze')
    parser.add_argument('-o', '--output', default='empty_run_analysis.csv',
                       help='Output CSV file (default: empty_run_analysis.csv)')
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Show only summary statistics')
    
    args = parser.parse_args()
    
    files = args.files
    
    if not args.quiet:
        print(f"Analyzing {len(files)} experiment files...")

    # Analyze each file
    results = []
    for filepath in files:
        try:
            result = analyze_experiment_file(filepath)
            results.append(result)
            if not args.quiet:
                print(f"  {result['experiment_id']}: {result['empty_runs']}/{result['total_runs']} ({result['empty_ratio']:.1%} empty)")
        except Exception as e:
            if not args.quiet:
                print(f"  Error analyzing {filepath}: {e}")

    # Sort by empty ratio (highest waste first)
    results.sort(key=lambda x: x['empty_ratio'], reverse=True)

    # Write to CSV
    output_file = args.output
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['experiment_id', 'total_runs', 'empty_runs', 'empty_ratio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    # Summary statistics
    if results:
        total_experiments = len(results)
        high_waste = sum(1 for r in results if r['empty_ratio'] > 0.8)
        medium_waste = sum(1 for r in results if 0.5 <= r['empty_ratio'] <= 0.8)
        low_waste = sum(1 for r in results if r['empty_ratio'] < 0.5)

        print(f"\n📊 Analysis Summary:")
        print(f"   Total experiments: {total_experiments}")
        print(f"   High waste (>80% empty): {high_waste}")
        print(f"   Medium waste (50-80% empty): {medium_waste}")
        print(f"   Low waste (<50% empty): {low_waste}")
        print(f"\n✓ Results saved to: {output_file}")
    else:
        print(f"No valid experiment files found.")


if __name__ == "__main__":
    main()
