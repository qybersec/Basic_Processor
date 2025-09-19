#!/usr/bin/env python3
"""
Simple Examples for TMS Processing

This file shows your boss how to use the core logic in different ways.
Perfect for ChatGPT to understand and adapt.
"""

from core_logic import TMSProcessor
import pandas as pd
import os

def example_1_basic_usage():
    """
    Example 1: Most Basic Usage
    Process one file, get output
    """
    print("=== Example 1: Basic Usage ===")

    processor = TMSProcessor()

    # Replace with actual file path
    input_file = "sample_report.xlsx"
    output_file = "processed_report.xlsx"

    try:
        # One-line processing
        df = processor.process_excel_file(input_file)
        processor.save_to_excel(df, output_file)

        print(f"✅ Processed {len(df)} records")
        print(f"💰 Total Savings: ${processor.summary_stats['total_potential_savings']:,.2f}")

    except FileNotFoundError:
        print("❌ File not found. Replace 'sample_report.xlsx' with your file path.")


def example_2_step_by_step():
    """
    Example 2: Step-by-Step Processing
    More control over each step
    """
    print("\n=== Example 2: Step-by-Step ===")

    processor = TMSProcessor()

    try:
        # Step 1: Load data
        df = processor.load_data("sample_report.xlsx")
        print(f"📄 Loaded {len(df)} records")

        # Step 2: Apply business rules
        df = processor.apply_business_rules(df)

        # Step 3: Calculate stats
        processor.calculate_summary_stats(df)

        # Step 4: Save
        processor.save_to_excel(df, "step_by_step_output.xlsx")

        print("✅ Step-by-step processing complete")

    except FileNotFoundError:
        print("❌ File not found. Replace with your file path.")


def example_3_custom_rules():
    """
    Example 3: Custom Business Rules
    Add your own rules easily
    """
    print("\n=== Example 3: Custom Rules ===")

    processor = TMSProcessor()

    try:
        # Load data
        df = processor.load_data("sample_report.xlsx")

        # Apply standard rules
        df = processor.apply_business_rules(df)

        # ADD YOUR CUSTOM RULE HERE
        # Example: Set savings to 0 for specific carriers
        custom_carriers = ['SPECIFIC CARRIER NAME']
        mask = df['Selected Carrier'].isin(custom_carriers)
        df.loc[mask, 'Potential Savings'] = 0
        print(f"🔧 Applied custom rule to {mask.sum()} records")

        # Save
        processor.save_to_excel(df, "custom_rules_output.xlsx")

        print("✅ Custom processing complete")

    except FileNotFoundError:
        print("❌ File not found. Replace with your file path.")


def example_4_batch_processing():
    """
    Example 4: Process Multiple Files
    Great for batch operations
    """
    print("\n=== Example 4: Batch Processing ===")

    # List of files to process
    input_files = [
        "file1.xlsx",
        "file2.xlsx",
        "file3.xlsx"
    ]

    processor = TMSProcessor()
    total_savings = 0

    for file_path in input_files:
        try:
            print(f"🔄 Processing: {file_path}")

            # Process file
            df = processor.process_excel_file(file_path)

            # Generate output name
            base_name = os.path.splitext(file_path)[0]
            output_file = f"{base_name}_PROCESSED.xlsx"

            # Save
            processor.save_to_excel(df, output_file)

            # Track totals
            savings = processor.summary_stats['total_potential_savings']
            total_savings += savings

            print(f"✅ {file_path}: ${savings:,.2f} savings")

        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")

    print(f"\n🎉 Batch complete! Total savings: ${total_savings:,.2f}")


def example_5_chatgpt_friendly():
    """
    Example 5: Perfect for ChatGPT Integration
    Very simple, clear structure
    """
    print("\n=== Example 5: ChatGPT-Friendly ===")

    # Initialize processor
    processor = TMSProcessor()

    # Customize settings (optional)
    processor.HEADER_ROW = 7  # Change if your headers are on different row
    processor.DATA_START_ROW = 10  # Change if your data starts elsewhere

    # Add custom TL carriers if needed
    processor.TL_CARRIERS.add('YOUR CUSTOM CARRIER')

    # Process file
    input_file = "your_file.xlsx"  # CHANGE THIS
    output_file = "processed_output.xlsx"  # CHANGE THIS

    try:
        # One command does everything
        df = processor.process_excel_file(input_file)
        processor.save_to_excel(df, output_file)

        # Print results
        stats = processor.summary_stats
        print(f"📊 Results:")
        print(f"   Loads processed: {stats['total_loads']:,}")
        print(f"   Total savings: ${stats['total_potential_savings']:,.2f}")
        print(f"   Average per load: ${stats['average_savings_per_load']:.2f}")
        print(f"   Savings percentage: {stats['percentage_savings']:.1f}%")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("🤖 TMS Processing Examples for Easy Integration")
    print("=" * 50)

    # Run all examples (will show errors for missing files, but that's OK)
    example_1_basic_usage()
    example_2_step_by_step()
    example_3_custom_rules()
    example_4_batch_processing()
    example_5_chatgpt_friendly()

    print("\n📝 Instructions for your boss:")
    print("1. Copy core_logic.py into your project")
    print("2. Use any example above as starting point")
    print("3. Modify file paths and rules as needed")
    print("4. ChatGPT can easily adapt these examples!")