import pandas as pd
import os
import sys

def load_sales_data():
    """Load Excel file - auto-detects environment and provides appropriate interface."""
    
    # Check if we're in Docker or have GUI capability
    in_docker = os.path.exists('/.dockerenv') or os.environ.get('DOCKER_CONTAINER')
    has_display = os.environ.get('DISPLAY') is not None and not in_docker
    
    if in_docker or not has_display:
        print("Docker/CLI Environment Detected")
        return load_sales_data_cli()
    else:
        print("Local GUI Environment Detected")
        return load_sales_data_gui()

def load_sales_data_gui():
    """Load Excel file using GUI (for local execution with display)."""
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
        
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        root.attributes('-topmost', True)  # Bring dialog to front
        
        file_path = filedialog.askopenfilename(
            title="Select Sales Excel File",
            filetypes=[
                ("Excel files", "*.xlsx *.xls"),
                ("All files", "*.*")
            ]
        )
        root.destroy()
        
        if file_path:
            print(f"Selected: {os.path.basename(file_path)}")
            return load_file(file_path)
        else:
            print("❌ No file selected. Switching to CLI mode...")
            return load_sales_data_cli()
            
    except Exception as e:
        print(f"⚠️ GUI failed: {e}. Switching to CLI mode...")
        return load_sales_data_cli()

def load_sales_data_cli():
    """Load Excel file using command line interface."""
    print("\nFile Selection")
    print("=" * 40)
    
    # Check for data directory
    data_dirs = ['/app/data', './data', '.']
    available_files = []
    
    for data_dir in data_dirs:
        if os.path.exists(data_dir):
            files = [f for f in os.listdir(data_dir) if f.endswith(('.xlsx', '.xls'))]
            if files:
                print(f"\nFound Excel files in {data_dir}:")
                for i, file in enumerate(files, 1):
                    print(f"   {i}. {file}")
                    available_files.append((data_dir, file))
    
    if available_files:
        print(f"\nSelect an option:")
        print("1. Choose from available files above")
        print("2. Enter custom file path")
        
        try:
            choice = input("Enter choice (1 or 2): ").strip()
            if choice == "1":
                file_num = int(input(f"Enter file number (1-{len(available_files)}): "))
                data_dir, file_name = available_files[file_num - 1]
                file_path = os.path.join(data_dir, file_name)
            else:
                file_path = input("Enter full file path: ").strip('" ')
        except (ValueError, IndexError):
            print("Invalid selection. Please enter custom file path.")
            file_path = input("Enter full file path: ").strip('" ')
    else:
        print("No Excel files found in data directories.")
        file_path = input("Enter full file path to Excel file: ").strip('" ')
    
    return load_file(file_path)

def load_file(file_path):
    """Common file loading logic."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully loaded {len(df)} rows from {os.path.basename(file_path)}")
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None