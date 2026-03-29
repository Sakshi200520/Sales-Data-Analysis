# ============================================
# 📊 Sales Data Analysis Project
# ============================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load dataset
try:
    df = pd.read_csv("sales_data (1).csv")
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: sales_data file not found! Check file path.")
    exit()

# Step 3: Display first few rows
print("📌 First 5 Rows of Dataset:")
print(df.head())

# Step 4: Explore dataset
print("\n📊 Dataset Information:")
df.info()

print("\n📐 Dataset Shape (Rows, Columns):")
print(df.shape)

print("\n📋 Column Names:")
print(df.columns)

# Step 5: Check missing values
print("\n❗ Missing Values in Each Column:")
print(df.isnull().sum())

# Step 6: Data Cleaning

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with 0
df = df.fillna(0)

print("\n✅ Data cleaned successfully!")

# Step 7: Data Analysis

# Ensure Total_Sales is numeric
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce').fillna(0)

# Calculate metrics
total_revenue = df['Total_Sales'].sum()
max_sales = df['Total_Sales'].max()
min_sales = df['Total_Sales'].min()
avg_sales = df['Total_Sales'].mean()

# Step 8: Best Selling Product
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
best_product = sales_by_product.idxmax()

# Step 9: Display Results
print("\n📈 ===== SALES ANALYSIS REPORT ===== 📈")

print(f"\n💰 Total Revenue: ₹{total_revenue:,.2f}")
print(f"📊 Average Sales: ₹{avg_sales:,.2f}")
print(f"📈 Highest Sale: ₹{max_sales:,.2f}")
print(f"📉 Lowest Sale: ₹{min_sales:,.2f}")

print(f"\n🏆 Best Selling Product: {best_product}")

print("\n📦 Sales by Product:")
print(sales_by_product)

# Step 10: Visualization (Bar Chart)
plt.figure()
sales_by_product.plot(kind='bar')

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# Step 11: Save report to file
try:
    with open("analysis_report.txt", "w", encoding="utf-8") as file:
        file.write("===== SALES ANALYSIS REPORT =====\n\n")
        file.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        file.write(f"Average Sales: ₹{avg_sales:,.2f}\n")
        file.write(f"Highest Sale: ₹{max_sales:,.2f}\n")
        file.write(f"Lowest Sale: ₹{min_sales:,.2f}\n")
        file.write(f"Best Selling Product: {best_product}\n\n")

        file.write("Sales by Product:\n")
        for product, sales in sales_by_product.items():
            file.write(f"{product}: ₹{sales:,.2f}\n")

    print("\n📄 Report saved as 'analysis_report.txt' successfully!")

except Exception as e:
    print("❌ Error while saving report:", e)

print("\n✅ Project Completed Successfully!")