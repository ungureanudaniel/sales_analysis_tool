import pandas as pd
import os

def load_sales_data():
    """Ask user for Excel file path and return a cleaned DataFrame."""
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
