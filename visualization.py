import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_top_products(summary, top_n=10):
    """Plot top N products by total sales."""
    if "Total_Sales" not in summary.columns:
        print("No Total_Sales column found.")
        return
    
    top_products = summary.head(top_n)
    
    # Set style
    plt.style.use('default')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Horizontal bar chart
    bars = ax1.barh(top_products["Article"], top_products["Total_Sales"], color="skyblue")
    ax1.set_xlabel("Total Sales", fontsize=12)
    ax1.set_ylabel("Product", fontsize=12)
    ax1.set_title(f"Top {top_n} Products by Sales", fontsize=14, fontweight='bold')
    
    # Add value labels on bars
    for bar in bars:
        width = bar.get_width()
        ax1.text(width, bar.get_y() + bar.get_height()/2, 
                f'{width:,.0f}', ha='left', va='center', fontsize=9)
    
    ax1.invert_yaxis()
    
    # Plot 2: Pie chart for sales distribution
    ax2.pie(top_products["Total_Sales"], labels=top_products["Article"], 
            autopct='%1.1f%%', startangle=90)
    ax2.set_title(f"Sales Distribution - Top {top_n} Products", fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    # Additional plot: Units vs Sales
    plt.figure(figsize=(10, 6))
    plt.scatter(summary['Total_Units_Sold'], summary['Total_Sales'], alpha=0.6)
    plt.xlabel('Total Units Sold')
    plt.ylabel('Total Sales')
    plt.title('Units Sold vs Total Sales')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_sales_comparison(summary, top_n=10):
    """Create a comparison plot showing units vs sales with direct article labels."""
    if all(col in summary.columns for col in ['Total_Sales', 'Total_Units_Sold', 'Article']):
        top_products = summary.head(top_n).copy()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Plot 1: Sales vs Units scatter plot with direct labels
        colors = plt.cm.Set3(np.linspace(0, 1, len(top_products)))
        
        for i, (idx, row) in enumerate(top_products.iterrows()):
            ax1.scatter(row['Total_Units_Sold'], row['Total_Sales'], 
                       s=120, alpha=0.8, color=colors[i], 
                       edgecolors='black', linewidth=0.8)
            
            # Place article code next to the point
            ax1.text(row['Total_Units_Sold'] + (row['Total_Units_Sold'] * 0.02), 
                    row['Total_Sales'], 
                    f"  {row['Article']}", 
                    fontsize=9, fontweight='bold', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                             alpha=0.8, edgecolor=colors[i], linewidth=1))
        
        ax1.set_xlabel('Total Units Sold', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Total Sales (€)', fontsize=12, fontweight='bold')
        ax1.set_title('Units Sold vs Total Sales\n(Article Codes Labeled)', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Price distribution with article codes
        if 'Average_Price' in summary.columns:
            bars = ax2.barh(top_products['Article'], top_products['Average_Price'], 
                           color=colors, edgecolor='black', linewidth=0.5)
            
            # Add price values on bars
            for bar, price, article in zip(bars, top_products['Average_Price'], top_products['Article']):
                width = bar.get_width()
                ax2.text(width + (width * 0.01), bar.get_y() + bar.get_height()/2, 
                        f'€{price:.2f}', ha='left', va='center', 
                        fontsize=8, fontweight='bold')
            
            ax2.set_xlabel('Average Price (€)', fontsize=12, fontweight='bold')
            ax2.set_ylabel('Product Article Code', fontsize=12, fontweight='bold')
            ax2.set_title('Average Price per Product', fontsize=14, fontweight='bold')
            ax2.grid(axis='x', alpha=0.3)
            ax2.invert_yaxis()
        
        plt.tight_layout()
        plt.show()