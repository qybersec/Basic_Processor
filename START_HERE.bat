@echo off
title Basic TMS Processor - One-Click Start
color 0A
echo.
echo  ████████╗███╗   ███╗███████╗    ██████╗ ██████╗  ██████╗  ██████╗███████╗███████╗███████╗ ██████╗ ██████╗
echo  ╚══██╔══╝████╗ ████║██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗
echo     ██║   ██╔████╔██║███████╗    ██████╔╝██████╔╝██║   ██║██║     █████╗  ███████╗███████╗██║   ██║██████╔╝
echo     ██║   ██║╚██╔╝██║╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║╚════██║██║   ██║██╔══██╗
echo     ██║   ██║ ╚═╝ ██║███████║    ██║     ██║  ██║╚██████╔╝╚██████╗███████╗███████║███████║╚██████╔╝██║  ██║
echo     ╚═╝   ╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
echo.
echo                                   🚀 ONE-CLICK BUSINESS LOGIC PROCESSOR 🚀
echo.
echo  ═══════════════════════════════════════════════════════════════════════════════════════════════════════════
echo.
echo  📊 FEATURES:
echo     ✅ Persistent Results Storage (survives app restart)
echo     ✅ Scrollable File Lists and Results
echo     ✅ Organized Output Folders (Basic_Processed_MM.DD_HHMM)
echo     ✅ Professional Excel Formatting
echo     ✅ Core TMS Business Rules Applied Automatically
echo.
echo  🤖 FOR DEVELOPERS:
echo     📁 core_logic.py      - Modular business logic (ChatGPT-friendly)
echo     📁 simple_examples.py - 5 usage patterns for AI adaptation
echo     📁 INTEGRATION_GUIDE.md - Complete AI integration guide
echo.
echo  ═══════════════════════════════════════════════════════════════════════════════════════════════════════════
echo.

:: Change to script directory
cd /d "%~dp0"

:: Check if Python is installed
echo  🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo  ❌ Error: Python is not installed or not in PATH
    echo     Please install Python 3.8+ from python.org
    echo.
    pause
    exit /b 1
)

:: Check if required packages are installed
echo  📦 Checking dependencies...
python -c "import pandas, openpyxl, tkinter" 2>nul
if errorlevel 1 (
    echo  🔄 Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo  ❌ Error: Failed to install dependencies
        echo     Please check your internet connection and try again
        echo.
        pause
        exit /b 1
    )
    echo  ✅ Dependencies installed successfully!
)

:: Run the main application
echo  🚀 Starting Basic TMS Processor...
echo.
python basic_processor.py

echo.
echo  ✅ Session complete!
echo     📁 Check your Results list for processing history
echo     🗂️ Multiple files are organized in timestamped folders
echo.
pause