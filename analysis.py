import pandas as pd

def summarize_sales(df):
    """Compute key sales metrics per product."""
    print(f"Starting analysis with {len(df)} rows...")
    print(f"Available columns: {list(df.columns)}")

    product_col = "Article"
    price_cols = ["     SPC1", "     SPC2"]
    qty_cols = ["Sales - 1", "Sales - 2", "Sales - 3", "Sales - 4", "Sales - 5", "Sales - 6", "Sales - 7", "Sales - 8"]
    
    # Debug: Check if expected columns exist - FIXED THIS PART
    missing_columns = []
    
    # Check product column
    if product_col not in df.columns:
        missing_columns.append(product_col)
    
    # Check price columns - only include missing ones
    missing_price_cols = [col for col in price_cols if col not in df.columns]
    missing_columns.extend(missing_price_cols)
    
    # Check quantity columns - only include missing ones
    missing_qty_cols = [col for col in qty_cols if col not in df.columns]
    missing_columns.extend(missing_qty_cols)

    if missing_columns:
        print(f"Missing expected columns: {missing_columns}")
        print("Please check your Excel file column names and update the analysis.py file accordingly.")
        return pd.DataFrame()  # Return empty DataFrame if critical columns are missing
        
    # Identify columns present in DataFrame
    print(f"Analyzing {len(df)} products...")
    print(f"All expected columns found!")
    print(f"Product column: {product_col}")
    print(f"Price columns: {price_cols}")
    print(f"Quantity columns: {qty_cols}")

    # Clean empty values - FIXED THIS PART
    print(f"\n🧹 Eliminating empty cells:")
    
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Remove rows with missing product names
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna(subset=[product_col])
    print(f"   Removed {initial_rows - len(df_clean)} rows with missing product names")
    
    # Remove rows where ALL price columns are NaN
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna(subset=price_cols, how='all')
    print(f"   Removed {initial_rows - len(df_clean)} rows with all price columns empty")
    
    # Remove rows where ALL quantity columns are NaN
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna(subset=qty_cols, how='all')
    print(f"   Removed {initial_rows - len(df_clean)} rows with all quantity columns empty")
    
    print(f"   Remaining rows: {len(df_clean)}")

    # Check data types
    print(f"\nData types:")
    for col in [product_col] + price_cols + qty_cols:
        print(f"  {col}: {df_clean[col].dtype}")

    # Convert numeric columns to appropriate types
    for col in price_cols + qty_cols:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # Compute metrics
    try:
        print(f"\nComputing metrics:")
        
        # Calculate total units sold (sum across all quantity columns)
        df_clean['Total_Units_Sold'] = df_clean[qty_cols].sum(axis=1, skipna=True)
        
        # Calculate average price (mean of price columns)
        df_clean['Average_Price'] = df_clean[price_cols].mean(axis=1, skipna=True)
        
        # Calculate total sales
        df_clean['Total_Sales'] = df_clean['Total_Units_Sold'] * df_clean['Average_Price']
        
        print(f"Calculations completed successfully")
        print(f"Sample calculations (first 3 rows):")
        sample_calc = df_clean[[product_col, 'Total_Units_Sold', 'Average_Price', 'Total_Sales']].head(3)
        print(sample_calc.to_string(float_format='%.2f', index=False))
    
    except Exception as e:
        print(f"❌ Error in calculations: {e}")
        import traceback
        traceback.print_exc()
        return None

    # Aggregate by product and create summary dataframe
    try:
        summary = df_clean.groupby(product_col).agg({
            'Total_Units_Sold': 'sum',
            'Total_Sales': 'sum',
            'Average_Price': 'mean'
        }).reset_index()

        summary = summary.sort_values('Total_Sales', ascending=False)

        print(f"\nSales Analysis Complete!")
        print(f"Total products analyzed: {len(summary)}")
        print(f"Total sales across all products: {summary['Total_Sales'].sum():,.2f}")

        print("\nTop 10 Products by Sales:")
        print(summary.head(10).to_string(index=False, float_format='%.2f'))

        # Show some statistics
        print(f"\nSales Statistics:")
        print(f"   Highest sales: {summary['Total_Sales'].max():,.2f}")
        print(f"   Average sales: {summary['Total_Sales'].mean():,.2f}")
        print(f"   Median sales: {summary['Total_Sales'].median():,.2f}")

        return summary
        
    except Exception as e:
        print(f"❌ Error in creating summary: {e}")
        import traceback
        traceback.print_exc()
        return None

# Test function for debugging
def test_with_sample_data():
    """Create sample data to test the analysis function."""
    print("Running test with sample data...")
    
    sample_data = {
        'Article': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B'],
        'SPC1': [10.0, 15.0, 20.0, 10.0, 15.0],
        'SPC2': [12.0, 16.0, 22.0, 12.0, 16.0],
        'Sales-1': [100, 50, 25, 80, 60],
        'Sales-2': [120, 55, 30, 90, 65],
        'Sales-3': [110, 52, 28, 85, 62],
        'Sales-4': [105, 53, 26, 88, 63],
        'Sales-5': [115, 54, 27, 87, 64],
        'Sales-6': [5, 54, 27, 27, 14],
        'Sales-7': [11, 8, 12, 47, 24],
        'Sales-8': [15, 4, 27, 37, 34]

    }
    
    df = pd.DataFrame(sample_data)
    result = summarize_sales(df)
    return result

if __name__ == "__main__":
    # Run test if file is executed directly
    test_with_sample_data()