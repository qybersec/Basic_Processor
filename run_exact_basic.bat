@echo off
title Exact Basic TMS Processor
echo ====================================
echo    Exact Basic TMS Processor
echo    Direct Copy from BVC_Automator
echo ====================================
echo.

:: Change to script directory
cd /d "%~dp0"

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

:: Check if required packages are installed
echo Checking dependencies...
python -c "import pandas, openpyxl" 2>nul
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

:: Run the exact processor
echo.
echo Starting Exact Basic TMS Processor...
echo This uses the EXACT same code as BVC_Automator's Basic Report
echo.
python exact_basic_processor.py

echo.
echo Processing complete. Press any key to exit...
pause >nul