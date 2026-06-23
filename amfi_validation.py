import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")

# AMFI codes available
fund_codes = set(df["amfi_code"].dropna().astype(str))

print("Total AMFI Codes:", len(fund_codes))

print("\nSample AMFI Codes:")
print(list(fund_codes)[:20])

print("\nValidation Completed")


import pandas as pd

df = pd.read_csv("data/processed/cleaned_data.csv")

print(df["amfi_code"].head(20))

print("\nUnique AMFI Sample:")
print(df["amfi_code"].dropna().unique()[:30])