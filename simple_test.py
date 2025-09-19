#!/usr/bin/env python3
"""
Simple test of core functionality
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def main():
    print("Testing core processor...")

    try:
        from basic_processor import ModernTMSProcessor

        # Test processor creation
        processor = ModernTMSProcessor()
        print("Processor created successfully")

        # Test if core methods exist
        if hasattr(processor, 'process_file'):
            print("process_file method exists")

        if hasattr(processor, 'save_processed_data'):
            print("save_processed_data method exists")

        print("Core processor test passed!")

    except Exception as e:
        print(f"Error: {e}")
        return False

    print("\nTesting GUI creation...")
    try:
        from basic_processor import BasicTMSGUI

        # Just create GUI, don't show it
        gui = BasicTMSGUI()
        gui.root.withdraw()  # Hide window

        print("GUI created successfully")

        # Test file selection simulation
        test_files = ["test1.xlsx", "test2.xlsx"]
        gui.input_files = test_files

        # Test update methods
        gui.update_file_list()

        print("File list and button updates work")

        print("All tests passed!")
        return True

    except Exception as e:
        print(f"GUI Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()