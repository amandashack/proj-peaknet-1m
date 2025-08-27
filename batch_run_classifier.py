#!/usr/bin/env python3
"""
LCLS Batch Classifier

General-purpose script that runs run_classifier.py sequentially on experiments 
from a CSV file, saving results to a specified directory. Works with any 
experiment type (crystallography, protein, materials, etc.).

Includes fault tolerance options to handle API failures gracefully and 
resume processing from partial progress without losing work.
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Run classification on multiple LCLS experiments from a CSV file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all experiments from CSV
  python batch_run_classifier.py experiments.csv

  # Process with fault tolerance (recommended for large batches)
  python batch_run_classifier.py experiments.csv --resume --timeout 2400

  # Process crystallography experiments (backward compatibility)
  python batch_run_classifier.py crystallography.csv --output-dir batch_crystallography_results

  # Process limited number with custom directories
  python batch_run_classifier.py protein_experiments.csv --output-dir protein_results --max-experiments 20

  # Force overwrite existing results
  python batch_run_classifier.py my_experiments.csv --force

  # Resume interrupted processing with extended timeout
  python batch_run_classifier.py large_experiments.csv --resume --timeout 3600
        """
    )

    # Required arguments
    parser.add_argument('csv_file', type=Path,
                       help='CSV file containing experiment IDs in the first column')

    # Optional arguments
    parser.add_argument('--output-dir', default='batch_results',
                       help='Directory to save classification results (default: batch_results)')
    parser.add_argument('--enrichment-dir', default='processed_experiments',
                       help='Directory containing enrichment markdown files (default: processed_experiments)')
    parser.add_argument('--max-experiments', type=int,
                       help='Maximum number of experiments to process (default: all)')
    parser.add_argument('--force', action='store_true',
                       help='Overwrite existing output files')
    
    # Fault tolerance options
    parser.add_argument('--resume', action='store_true',
                       help='Enable fault tolerance - continue processing despite API failures and resume from partial progress')
    parser.add_argument('--timeout', type=int, default=1800,
                       help='Timeout per experiment in seconds (default: 1800 = 30 min). Use 2400+ for large experiments')

    args = parser.parse_args()

    print("🔬 LCLS Batch Classifier")
    print("=" * 50)

    # Validate input CSV file
    if not args.csv_file.exists():
        print(f"❌ Error: CSV file not found: {args.csv_file}")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_path = Path(args.output_dir)
    output_path.mkdir(exist_ok=True)
    print(f"✓ Output directory: {args.output_dir}/")
    if args.resume:
        print(f"✓ Fault tolerance enabled - will continue on API failures and resume from partial progress")
    if args.timeout != 1800:
        print(f"✓ Timeout per experiment: {args.timeout} seconds ({args.timeout//60} minutes)")

    # Read experiment IDs from CSV
    experiment_ids = []
    try:
        with open(args.csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if row and row[0].strip():  # Skip empty rows
                    experiment_ids.append(row[0].strip())
    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
        sys.exit(1)

    # Limit experiments if specified
    if args.max_experiments:
        experiment_ids = experiment_ids[:args.max_experiments]
        print(f"✓ Limited to first {len(experiment_ids)} experiments (--max-experiments {args.max_experiments})")
    else:
        print(f"✓ Processing all {len(experiment_ids)} experiments from {args.csv_file}")
    print()

    # Process each experiment
    processed_count = 0
    skipped_count = 0

    for i, exp_id in enumerate(experiment_ids, 1):
        print(f"[{i:2d}/{len(experiment_ids)}] Processing: {exp_id}")

        # Check if enrichment file exists
        enrichment_file = Path(args.enrichment_dir) / f"{exp_id}_enrichment.md"
        output_file = output_path / f"{exp_id}_classifications.json"

        if not enrichment_file.exists():
            print(f"  ⚠️  Skipped - enrichment file not found: {enrichment_file}")
            skipped_count += 1
            continue

        # Check if output already exists (skip unless --force)
        if output_file.exists() and not args.force:
            print(f"  ⚠️  Skipped - output already exists: {output_file} (use --force to overwrite)")
            skipped_count += 1
            continue

        # Run classifier
        try:
            cmd = [
                "python", "run_classifier.py",
                str(enrichment_file),
                "-o", str(output_file)
            ]
            
            # Add fault tolerance flag if requested
            if args.resume:
                cmd.append("--resume")

            print(f"  🚀 Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout)

            if result.returncode == 0:
                print(f"  ✅ Completed: {output_file}")
                processed_count += 1
            else:
                print(f"  ❌ Failed with return code {result.returncode}")
                if result.stderr:
                    print(f"     Error: {result.stderr.strip()}")
                # Check if partial results were produced despite failure
                if output_file.exists():
                    print(f"     Note: Partial results may be available at {output_file}")
                    if args.resume:
                        print(f"     Use --resume to continue from partial progress")
                skipped_count += 1

        except subprocess.TimeoutExpired:
            print(f"  ⏰ Timeout after {args.timeout//60} minutes - skipping {exp_id}")
            if args.resume:
                print(f"     Note: Use --resume to continue from partial progress if available")
            skipped_count += 1
        except Exception as e:
            print(f"  ❌ Error running classifier: {e}")
            skipped_count += 1

        print()

    # Summary
    print("=" * 50)
    print("📊 BATCH PROCESSING COMPLETE")
    print(f"✅ Successfully processed: {processed_count}")
    print(f"⚠️  Skipped: {skipped_count}")
    print(f"📁 Results saved to: {args.output_dir}/")

    if processed_count > 0:
        print(f"\n🔍 To analyze results:")
        print(f"   ls {args.output_dir}/*.json")
        print(f"   python token_summary.py {args.output_dir}/*.json --detailed --cost")
        print(f"   # Each file contains token usage data in processing_info.token_usage")

        print(f"\n🔄 To create fully enriched documents:")
        print(f"   python batch_fill_enrichment.py --classification-dir {args.output_dir}")

    if skipped_count > 0 and args.resume:
        print(f"\n♾️ To retry failed experiments with fault tolerance:")
        print(f"   python batch_run_classifier.py {args.csv_file} --output-dir {args.output_dir} --resume --timeout {max(args.timeout, 2400)}")
        print(f"   # Increase timeout for problematic experiments")


if __name__ == "__main__":
    main()
