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