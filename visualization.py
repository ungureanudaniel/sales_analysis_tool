import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_top_products(summary, top_n=10):
    """Plot top N products by total sales with enhanced styling."""
    if "Total_Sales" not in summary.columns or "Article" not in summary.columns:
        print("Required columns not found.")
        return
    
    top_products = summary.head(top_n).copy()
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Plot 1: Horizontal bar chart
    y_pos = np.arange(len(top_products))
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_products)))
    
    bars = ax1.barh(y_pos, top_products["Total_Sales"], color=colors, height=0.8, 
                   edgecolor='black', linewidth=0.5)
    
    # Customize bar chart
    ax1.set_xlabel("Total Sales (€)", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Product Article Code", fontsize=12, fontweight='bold')
    ax1.set_title(f"Top {top_n} Products by Sales", fontsize=14, fontweight='bold', pad=20)
    
    # Set y-axis ticks and labels
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(top_products["Article"], fontsize=10)
    
    # Add value labels on bars
    for bar, value in zip(bars, top_products["Total_Sales"]):
        width = bar.get_width()
        ax1.text(width + (width * 0.01), bar.get_y() + bar.get_height()/2, 
                f'€{value:,.0f}', ha='left', va='center', 
                fontsize=10, fontweight='bold', color='darkblue')
    
    ax1.invert_yaxis()  # Highest sales at top
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Plot 2: Donut chart (better than pie chart)
    wedges, texts, autotexts = ax2.pie(top_products["Total_Sales"], 
                                      labels=top_products["Article"], 
                                      autopct='%1.1f%%', 
                                      startangle=90,
                                      colors=colors,
                                      wedgeprops={'edgecolor': 'black', 'linewidth': 0.5})
    
    # Make it a donut chart
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    ax2.add_artist(centre_circle)
    
    # Style the labels
    for text in texts:
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
        autotext.set_color('black')
    
    ax2.set_title(f"Sales Distribution - Top {top_n} Products", fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.show()

def plot_sales_comparison(summary, top_n=10):
    """Plot sales vs units with article codes."""
    if not all(col in summary.columns for col in ['Total_Sales', 'Total_Units_Sold', 'Article']):
        print("Required columns for scatter plot not found.")
        print(f"Available columns: {list(summary.columns)}")
        return
    
    top_products = summary.head(top_n).copy()
    
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot with article codes - SIMPLE VERSION
    plt.scatter(top_products['Total_Units_Sold'], top_products['Total_Sales'], 
               s=100, alpha=0.7, color='blue', edgecolors='black')
    
    # Add article codes as labels
    for i, row in top_products.iterrows():
        plt.text(row['Total_Units_Sold'] + (row['Total_Units_Sold'] * 0.02), 
                row['Total_Sales'], 
                f"{row['Article']}", 
                fontsize=9, fontweight='bold', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', 
                         alpha=0.7, edgecolor='black'))
    
    plt.xlabel('Total Units Sold', fontsize=12, fontweight='bold')
    plt.ylabel('Total Sales (€)', fontsize=12, fontweight='bold')
    plt.title('Total Sales vs Total Units Sold', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Or even simpler version:
def plot_sales_comparison_simple(summary, top_n=10):
    """Simple scatter plot without fancy colors."""
    if not all(col in summary.columns for col in ['Total_Sales', 'Total_Units_Sold', 'Article']):
        print("Required columns for scatter plot not found.")
        return
    
    top_products = summary.head(top_n)
    
    plt.figure(figsize=(12, 8))
    
    # Basic scatter plot
    plt.scatter(top_products['Total_Units_Sold'], top_products['Total_Sales'], 
               alpha=0.6, color='red')
    
    # Add labels
    for i, row in top_products.iterrows():
        plt.annotate(row['Article'], 
                    (row['Total_Units_Sold'], row['Total_Sales']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8)
    
    plt.xlabel('Total Units Sold')
    plt.ylabel('Total Sales')
    plt.title('Sales vs Units Sold')
    plt.grid(True)
    plt.show()
