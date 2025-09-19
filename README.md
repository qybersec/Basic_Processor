# Basic TMS Processor

A simplified version of the BVC_Automator that focuses only on the core TMS business logic for processing transportation data reports.

## 🚀 Quick Start

1. **Double-click** `run_basic_processor.bat`
2. **Enter** the path to your Excel file when prompted
3. **Wait** for processing to complete
4. **Find** your processed file with `_BASIC_PROCESSED.xlsx` suffix

## 📋 What It Does

### Core Business Rules Applied:
- **Same Carrier Rule**: Sets potential savings to $0 when selected carrier equals least cost carrier
- **Empty Data Rule**: Copies selected carrier data to least cost when least cost data is missing
- **Negative Savings Rule**: Fixes negative potential savings by copying selected data
- **TL Carriers Rule**: Special handling for LANDSTAR and SMARTWAY carriers
- **Professional Formatting**: Color-coded Excel output with summary statistics

### Input Requirements:
- Excel file (.xlsx) with TMS data
- Headers on row 8, data starting on row 11
- Standard TMS column structure (Load No., carriers, costs, etc.)

### Output Features:
- **Main Report**: Processed data with color-coded sections
  - 🔵 Selected Carrier columns (light blue)
  - 🟠 Least Cost Carrier columns (light orange)
  - 🟢 Potential Savings column (light green)
- **Summary Statistics**: Key metrics and totals on separate sheet

## 🛠️ Technical Details

### Dependencies:
- Python 3.8+
- pandas >= 1.3.0
- openpyxl >= 3.0.0

### Manual Installation:
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

**Removed Complex Features:**
- ❌ Advanced GUI interface
- ❌ Complex logging system
- ❌ Advanced validation framework
- ❌ Configuration management
- ❌ Multiple report types
- ❌ Advanced error handling UI

## 📁 Files

- `basic_processor.py` - Main processing logic
- `run_basic_processor.bat` - Windows batch runner
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

---

**Simplified from BVC_Automator for focused TMS report processing**