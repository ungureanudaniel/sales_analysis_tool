from data_loader import load_sales_data
from analysis import summarize_sales
from visualization import plot_top_products, plot_sales_trends

def main():
    print("🚀 Carrefour Sales Analysis Tool")
    print("=" * 40)
    
    # Load data
    df = load_sales_data()
    
    if df is not None:
        # Analyze data
        summary = summarize_sales(df)
        
        # Visualize results
        plot_top_products(summary, top_n=10)
        plot_sales_trends(df)
        
        print("\n✅ Analysis complete! Check the charts for insights.")

if __name__ == "__main__":
    main()