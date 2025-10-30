Carrefour Sales Analysis Tool
A Python-based sales analysis tool for analyzing Carrefour product sales data. This tool automatically processes Excel files, generates sales effectiveness reports, and creates comprehensive visualizations.

Features
📊 Automated Sales Analysis: Process Excel files with product sales data

📈 Interactive Visualizations: Generate bar charts, scatter plots, and trend analysis

🎯 Product Performance Metrics: Identify top-performing products by sales and units

📋 Multiple Chart Types: Horizontal bars, scatter plots, donut charts, and trend lines

🐳 Docker Support: Easy deployment using Docker Compose

Prerequisites
For Docker Deployment (Recommended)
Docker Desktop for Windows

Git

For Local Development
Python 3.8+

pip (Python package manager)

Quick Start with Docker
1. Install Docker on Windows
Download Docker Desktop from Docker's official website

Run the installer and follow the setup wizard

Restart your computer when prompted

Open Docker Desktop and ensure it's running

2. Clone and Run the Application
bash
# Clone the repository
git clone https://github.com/your-username/carrefour-sales-analysis.git
cd carrefour-sales-analysis

# Start the application using Docker Compose
docker-compose up --build -d
3. Using the Application
The application will start and prompt you for an Excel file path.

Copy the excel file path, by clicking right and pressing "Copy as path".

View the generated charts and analysis in the console output.

Project Structure
text
carrefour-sales-analysis/
├── data/                   # Place your Excel files here
├── src/
│   ├── data_loader.py     # Excel file loading module
│   ├── analysis.py        # Sales analysis logic
│   ├── visualization.py   # Chart generation module
│   └── main.py           # Main application entry point
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
Manual Installation (Without Docker)
1. Clone the Repository
bash
git clone https://github.com/your-username/carrefour-sales-analysis.git
cd carrefour-sales-analysis
2. Create Virtual Environment
bash
# Create virtual environment
python -m venv myvenv

# Activate virtual environment
# For Windows PowerShell:
./myvenv/Scripts/Activate
# For Windows Command Prompt:
./myvenv/Scripts/activate.bat
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the Application (when inside the project folder)
bash
python main.py
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
Docker Configuration Files
Dockerfile
dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/

VOLUME /app/data

CMD ["python", "src/main.py"]
docker-compose.yml
yaml
version: '3.8'

services:
  sales-analysis:
    build: .
    container_name: carrefour-sales-analysis
    volumes:
      - ./data:/app/data:rw
    stdin_open: true
    tty: true
Output
The application generates:

Console Output: Summary statistics and top products

Visualizations:

Top products by sales (horizontal bar chart)

Sales vs units sold scatter plot with article codes

Sales distribution (donut chart)

Price analysis

Sales trends across periods

Troubleshooting
Common Docker Issues
Docker not starting:

Ensure virtualization is enabled in BIOS

Run Docker Desktop as administrator

Permission errors on Windows:

Share drives in Docker Desktop settings

Run Docker with elevated privileges

Excel file not found:

Ensure file is in the data/ directory

Check file path case sensitivity

Common Python Issues
Missing dependencies:

bash
pip install --upgrade pip
pip install -r requirements.txt
Excel file format issues:

Ensure columns match expected names

Check for empty rows or columns

Development
Adding New Features
Modify the analysis modules in src/

Update requirements if adding new dependencies

Test with sample data

Rebuild Docker image if needed: docker-compose build --no-cache

Sample Data
Create a test Excel file in the data/ directory with sample sales data to verify the installation.

Support
For issues and questions:

Check the troubleshooting section above

Ensure your Excel file matches the expected format

Verify all prerequisites are installed correctly

License
This project is licensed under the MIT License - see the LICENSE file for details.