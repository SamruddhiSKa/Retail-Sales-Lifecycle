import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/retail_sales_cleaned.csv")

# Add Revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# 1. Top selling products
product_sales = df.groupby('Product')['Quantity'].sum()
product_sales.plot(kind='bar', title='Top Selling Products')
plt.show()

# 2. Revenue trend by date
df['Date'] = pd.to_datetime(df['Date'])
daily_revenue = df.groupby('Date')['Revenue'].sum()
daily_revenue.plot(kind='line', marker='o', title='Daily Revenue Trend')
plt.show()
