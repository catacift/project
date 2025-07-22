# Electricity Sales Analysis by State

## Description
This Python project analyzes electricity sales data by U.S. state using an Excel file with multi-level headers. It reads, processes, and visualizes total electricity sales (in Megawatt-hours) per state.

## Setup

### Prerequisites
- Python 3.x installed
- Recommended to use a virtual environment (e.g., `venv` in PyCharm)
- Install dependencies:
```bash
pip install pandas matplotlib
Running the Project in PyCharm
Open this project folder in PyCharm.

Make sure your Python interpreter is set to the project’s virtual environment.

Place your sales2023.xlsx file in your desired directory.

Update the file path in the script accordingly.

Run the Python script (your_script_name.py) from PyCharm.

Script Overview
Reads the Excel file with 3 header rows.

Flattens multi-level headers.

Aggregates total sales by state.

Prints summary to console.

Generates a bar chart of total electricity sales per state.
/your-project-folder
│
├── sales2023.xlsx           # Your data file (not included in repo)
/ ├── your_script_name.py     # Main analysis script
└── README.md                # This documentation
Notes
Modify the file_path variable in the script to your local Excel file path.

Ensure the Excel file follows the expected multi-header format.

License
MIT License