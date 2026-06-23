import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_mutual_fund_data.csv", low_memory=False)

print("=== DATA QUALITY SUMMARY ===")

# Shape
print("\nTotal Rows:")
print(df.shape[0])

print("\nTotal Columns:")
print(df.shape[1])

# Missing values
print("\nTop 10 Missing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes.head(10))

print("\nData Quality Check Completed")