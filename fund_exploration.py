import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")

print("\n=== UNIQUE FUND HOUSES ===")
print(df["fund_house"].dropna().unique())

print("\nTotal Fund Houses:")
print(df["fund_house"].nunique())

print("\n=== UNIQUE CATEGORIES ===")
print(df["category"].dropna().unique())

print("\n=== UNIQUE SUB-CATEGORIES ===")
print(df["sub_category"].dropna().unique())

print("\n=== UNIQUE RISK GRADES ===")
print(df["risk_grade"].dropna().unique())

print("\n=== SAMPLE AMFI CODES ===")
print(df["amfi_code"].dropna().unique()[:20])

print("\nFund Exploration Completed")