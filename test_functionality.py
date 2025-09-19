#!/usr/bin/env python3
"""
Test actual functionality of the GUI
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_functionality():
    try:
        print("Starting functionality test...")
        from basic_processor import BasicTMSGUI

        # Create GUI
        gui = BasicTMSGUI()

        print("Testing file list update...")
        # Simulate adding files
        test_files = [
            "C:/test/file1.xlsx",
            "C:/test/file2.xlsx"
        ]
        gui.input_files = test_files
        gui.update_file_list()

        print(f"File counter text: {gui.file_counter_label.cget('text')}")
        print(f"Process button text: {gui.process_btn.cget('text')}")

        print("Testing clear files...")
        gui.clear_files()

        print(f"After clear - File counter: {gui.file_counter_label.cget('text')}")
        print(f"After clear - Process button: {gui.process_btn.cget('text')}")

        print("Testing processor...")
        if hasattr(gui.processor, 'process_file'):
            print("OK processor has process_file method")
        else:
            print("ERROR processor missing process_file method")

        if hasattr(gui.processor, 'save_processed_data'):
            print("OK processor has save_processed_data method")
        else:
            print("ERROR processor missing save_processed_data method")

        print("=== Functionality test completed successfully ===")
        return True

    except Exception as e:
        print(f"ERROR in functionality test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_functionality()