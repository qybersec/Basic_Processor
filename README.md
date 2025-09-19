# Basic TMS Processor

A simplified version of the BVC_Automator that focuses only on the core TMS business logic for processing transportation data reports.

## 🚀 Quick Start

### One-Click Launch
1. **Double-click** `START_HERE.bat` (recommended)
2. **Select files** using the Browse button
3. **Click Process** and wait for completion
4. **Check Results list** for processing history (persists between sessions)

### Alternative Launch
1. **Double-click** `run_basic_processor.bat`
2. Follow the same steps above

## 📋 What It Does

### Core Business Rules Applied

- **Same Carrier Rule**: Sets potential savings to $0 when selected carrier equals least cost carrier
- **Empty Data Rule**: Copies selected carrier data to least cost when least cost data is missing
- **Negative Savings Rule**: Fixes negative potential savings by copying selected data
- **TL Carriers Rule**: Special handling for LANDSTAR and SMARTWAY carriers
- **Professional Formatting**: Color-coded Excel output with summary statistics

### Input Requirements

- Excel file (.xlsx) with TMS data
- Headers on row 8, data starting on row 11
- Standard TMS column structure (Load No., carriers, costs, etc.)

### Output Features

- **Main Report**: Processed data with color-coded sections
  - 🔵 Selected Carrier columns (light blue)
  - 🟠 Least Cost Carrier columns (light orange)
  - 🟢 Potential Savings column (light green)
- **Summary Statistics**: Key metrics and totals on separate sheet

## 🛠️ Technical Details

### Dependencies

- Python 3.8+
- pandas >= 1.3.0
- openpyxl >= 3.0.0

### Manual Installation

```bash
pip install pandas openpyxl
python basic_processor.py path/to/your/file.xlsx
```

## 📊 Expected File Structure

Your Excel file should have:

- Row 4, Column B: Company name
- Row 6, Column B: Date range
- Row 8: Column headers
- Row 11+: Data rows

## 🔍 Key Differences from BVC_Automator

**Simplified Features:**

- ✅ Core business logic rules
- ✅ Professional Excel formatting
- ✅ Summary statistics
- ✅ Command-line interface

## 🤖 For AI Integration / Developers

**Perfect for ChatGPT, Claude, or any AI assistant to adapt:**

### Quick Integration (30 seconds)
```python
# Copy core_logic.py to your project
from core_logic import TMSProcessor

processor = TMSProcessor()
df = processor.process_excel_file("your_file.xlsx")
processor.save_to_excel(df, "output.xlsx")
```

### Key Files for Integration
- **`core_logic.py`** - Modular business logic (AI-friendly)
- **`simple_examples.py`** - 5 usage patterns
- **`INTEGRATION_GUIDE.md`** - Complete AI adaptation guide

### AI Assistant Instructions
The code is designed for easy AI understanding:
- ✅ Clean, documented functions
- ✅ Modular business rules
- ✅ Simple examples provided
- ✅ Customization points clearly marked

## 📁 Files

### Main Application
- `START_HERE.bat` - **One-click launcher (RECOMMENDED)**
- `basic_processor.py` - Full GUI application with persistent results
- `run_basic_processor.bat` - Alternative launcher
- `requirements.txt` - Python dependencies

### Integration Files (for developers/AI)
- `core_logic.py` - Modular business logic class
- `simple_examples.py` - 5 different usage examples
- `INTEGRATION_GUIDE.md` - Complete integration documentation

### Support Files
- `logger_config.py` - Logging utilities
- `README.md` - This documentation

