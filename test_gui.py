#!/usr/bin/env python3
"""
Test script to check GUI functionality
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_gui():
    try:
        print("1. Testing imports...")
        from basic_processor import BasicTMSGUI
        print("OK Imports successful")

        print("2. Creating GUI...")
        gui = BasicTMSGUI()
        print("OK GUI created successfully")

        print("3. Testing file selection method...")
        # Test if the method exists and is callable
        if hasattr(gui, 'select_files') and callable(gui.select_files):
            print("OK select_files method exists")
        else:
            print("ERROR select_files method missing or not callable")

        print("4. Testing process method...")
        if hasattr(gui, 'process_files') and callable(gui.process_files):
            print("OK process_files method exists")
        else:
            print("ERROR process_files method missing or not callable")

        print("5. Testing processor...")
        if hasattr(gui, 'processor') and gui.processor:
            print("OK processor object exists")
        else:
            print("ERROR processor object missing")

        print("6. Testing UI components...")
        if hasattr(gui, 'process_btn'):
            print("OK process_btn exists")
        else:
            print("ERROR process_btn missing")

        if hasattr(gui, 'browse_btn'):
            print("OK browse_btn exists")
        else:
            print("ERROR browse_btn missing")

        print("\n=== Test completed ===")
        return True

    except Exception as e:
        print(f"ERROR during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_gui()