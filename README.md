# Sales Analysis Tool

A Python-based sales analysis tool for analyzing product sales data with a user-friendly GUI interface. This tool automatically processes Excel files, generates sales effectiveness reports, and creates comprehensive visualizations.

## Features

- 🖼️ **Easy GUI Interface** - File picker dialog for easy file selection
- 📊 **Automated Sales Analysis** - Process Excel files with product sales data
- 📈 **Interactive Visualizations** - Generate bar charts, scatter plots, and trend analysis
- 🎯 **Product Performance Metrics** - Identify top-performing products by sales and units
- 📋 **Multiple Chart Types** - Horizontal bars, scatter plots, donut charts, and trend lines

## Quick Start (Recommended - Local Python)

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/ungureanudaniel/sales-analysis-tool.git
cd sales-analysis-tool

# Install required packages
pip install -r requirements.txt
3. Run the Application
bash
python main.py
4. Using the Application
File Selection: A file picker dialog will automatically open

Choose Excel File: Select your sales data Excel file

View Results: The analysis will run automatically and display charts

Navigate Charts: Close each chart window to see the next one

Project Structure
text
sales-analysis-tool/
├── data/                   # Optional: Place your Excel files here
├── src/
│   ├── data_loader.py     # Excel file loading with GUI
│   ├── analysis.py        # Sales analysis logic
│   ├── visualization.py   # Chart generation module
│   └── main.py           # Main application entry point
├── requirements.txt
└── README.md
Excel File Format
Your Excel file should contain the following columns:

Article: Product identifier/code

SPC1, SPC2: Price columns

Sales-1 to Sales-8: Sales quantity columns for different periods

Example structure:
text
Article    SPC1   SPC2   Sales-1   Sales-2   ...   Sales-8
107251098  15.99  16.99  100       120       ...   115
107295766  12.50  13.00  80        90        ...   87
Output
The application generates:

Console Output: Summary statistics and top products

Visualizations (in this order):

Top products by sales (horizontal bar chart)

Sales distribution (donut chart)

Sales vs units sold scatter plot with article codes

Sales trends across periods

Manual File Selection (Alternative)
If the GUI file picker doesn't work, you can manually enter the file path:

Run: python main.py

When prompted, enter the full path to your Excel file

You can get the path by right-clicking the file in File Explorer and selecting "Copy as path"
