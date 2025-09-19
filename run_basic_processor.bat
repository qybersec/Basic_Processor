@echo off
title Basic TMS Processor
echo ====================================
echo    Basic TMS Processor
echo    Simplified BVC_Automator
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

:: Run the GUI processor
echo.
echo Starting Basic TMS Processor GUI...
echo.
python basic_processor.py

echo.
echo Processing complete. Press any key to exit...
pause >nul