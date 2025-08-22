import pandas as pd

# Load dataset
df = pd.read_csv("data/retail_sales.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Drop duplicates if any
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("data/retail_sales_cleaned.csv", index=False)

print("✅ Cleaned dataset saved as data/retail_sales_cleaned.csv")
