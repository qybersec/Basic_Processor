# Integration Guide for TMS Business Logic

## 🎯 For Your Boss / AI Integration

This guide explains how to integrate the TMS business logic into any Python project. Perfect for ChatGPT, Claude, or any AI assistant to understand and adapt.

## 📁 Key Files for Integration

### Core Files (Required)
- **`core_logic.py`** - Main business logic class
- **`simple_examples.py`** - 5 different usage examples
- **`requirements.txt`** - Dependencies (pandas, openpyxl)

### Optional Files
- **`basic_processor.py`** - Full GUI version (if UI needed)
- **`logger_config.py`** - Logging utilities

## 🚀 Quick Start (30 seconds)

### 1. Copy Files
```bash
# Copy these 3 files to your project:
core_logic.py
simple_examples.py
requirements.txt
```

### 2. Install Dependencies
```bash
pip install pandas openpyxl
```

### 3. Basic Usage
```python
from core_logic import TMSProcessor

# One-liner processing
processor = TMSProcessor()
df = processor.process_excel_file("your_file.xlsx")
processor.save_to_excel(df, "output.xlsx")

# Check results
print(f"Savings: ${processor.summary_stats['total_potential_savings']:,.2f}")
```

## 🧠 AI Assistant Instructions

### For ChatGPT/Claude Integration:

```
You are helping adapt TMS business logic. Here's what you need to know:

CORE CLASS: TMSProcessor from core_logic.py
- process_excel_file(path) -> processes everything
- load_data(path) -> just loads and cleans
- apply_business_rules(df) -> just applies rules
- save_to_excel(df, path) -> saves with formatting

BUSINESS RULES (all automatic):
1. Same carrier rule: PS = 0 when selected = least cost
2. Empty data rule: Copy selected to least cost when missing
3. Negative savings rule: Fix negative PS values
4. TL carriers rule: Special LANDSTAR/SMARTWAY handling

CUSTOMIZATION POINTS:
- processor.HEADER_ROW = 7 (change if different)
- processor.DATA_START_ROW = 10 (change if different)
- processor.TL_CARRIERS.add('NEW CARRIER') (add carriers)

EXAMPLES: See simple_examples.py for 5 different patterns
```

## 🔧 Common Customizations

### Change File Structure
```python
processor = TMSProcessor()
processor.HEADER_ROW = 5        # Headers on row 6
processor.DATA_START_ROW = 8    # Data starts row 9
```

### Add Custom Carriers
```python
processor = TMSProcessor()
processor.TL_CARRIERS.add('YOUR SPECIAL CARRIER')
processor.TL_CARRIERS.add('ANOTHER CARRIER')
```

### Add Custom Business Rule
```python
# After loading data
df = processor.load_data("file.xlsx")
df = processor.apply_business_rules(df)

# Add your custom rule
mask = df['Selected Carrier'].str.contains('CUSTOM PATTERN')
df.loc[mask, 'Potential Savings'] = 0

# Continue processing
processor.save_to_excel(df, "output.xlsx")
```

## 📊 Understanding the Business Rules

### Rule 1: Same Carrier
**What**: When Selected Carrier = Least Cost Carrier
**Action**: Set Potential Savings = $0
**Why**: No savings possible if already using cheapest option

### Rule 2: Empty Data
**What**: When Least Cost Carrier is blank/missing
**Action**: Copy all Selected data to Least Cost columns, PS = $0
**Why**: Can't compare savings without least cost data

### Rule 3: Negative Savings
**What**: When Potential Savings < $0 (selected cheaper than "least cost")
**Action**: Copy Selected to Least Cost, PS = $0
**Why**: Negative savings indicates data error

### Rule 4: TL Carriers
**What**: When Selected/Least Cost is LANDSTAR or SMARTWAY
**Action**: Copy Selected to Least Cost, PS = $0
**Why**: These carriers have special contract terms

## 🔍 Data Structure Expected

### Input Excel Format:
- **Row 4, Column B**: Company name
- **Row 6, Column B**: Date range
- **Row 8**: Headers (Load No., carriers, costs, etc.)
- **Row 11+**: Data rows

### Key Columns:
- Load No.
- Selected Carrier, Selected Service Type, Selected Total Cost
- Least Cost Carrier, Least Cost Service Type, Least Cost Total Cost
- PS or Potential Savings

## 💡 Integration Patterns

### Pattern 1: Simple Replacement
Replace your existing TMS logic with:
```python
from core_logic import TMSProcessor
processor = TMSProcessor()
df = processor.process_excel_file(input_file)
processor.save_to_excel(df, output_file)
```

### Pattern 2: Custom Pipeline
```python
processor = TMSProcessor()
df = processor.load_data(input_file)
# Your custom processing here
df = processor.apply_business_rules(df)
# More custom processing
processor.save_to_excel(df, output_file)
```

### Pattern 3: Rule-by-Rule
```python
processor = TMSProcessor()
df = processor.load_data(input_file)
df = processor._apply_same_carrier_rule(df)
df = processor._apply_empty_data_rule(df)
# Skip other rules if not needed
processor.save_to_excel(df, output_file)
```

## 🤖 AI Adaptation Tips

### For ChatGPT/Claude:
1. **Show the examples**: Copy simple_examples.py content into prompt
2. **Specify customizations**: "Change header row to 5, add carrier XYZ"
3. **Request specific pattern**: "Use Pattern 2 with custom validation step"

### For Code Generation:
- The class is fully documented with docstrings
- Each method has clear inputs/outputs
- Error handling is built-in
- Examples cover all common scenarios

## 🔗 Support

If your boss needs help:
1. **Check simple_examples.py** - covers 90% of use cases
2. **Review core_logic.py** - well-documented, easy to modify
3. **AI assistants can easily adapt** - designed for this purpose

The code is intentionally simple and modular for easy AI understanding and adaptation!