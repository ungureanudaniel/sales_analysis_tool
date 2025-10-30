import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file_gui():
    """Open a file dialog to select an Excel file and return its path."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select Sales Excel File",
        filetypes=[
            ("Excel files", "*.xlsx *.xls"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        messagebox.showwarning("No file selected", "Please select an Excel file to proceed.")
        return None
    return file_path

def load_sales_data():
    """Ask user for Excel file path and return a cleaned DataFrame."""
    file_path = select_file_gui()
    if not file_path:
        return None

    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path and try again.")
        return None
    
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Successfully loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"⚠️ Error loading Excel file: {e}")
        return None

def load_sales_data_cli():
    """Fallback CLI method for file loading."""
    file_path = input("Enter the path to your Excel file: ").strip('" ')
    
    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path and try again.")
        return None
    
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Successfully loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"⚠️ Error loading Excel file: {e}")
        return None
