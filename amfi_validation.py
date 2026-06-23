import pandas as pd

df = pd.read_csv("cleaned_mutual_fund_data.csv", low_memory=False)

fund_codes = set(df["amfi_code"].dropna().astype(str))

print("Total AMFI Codes:", len(fund_codes))

print("\nSample AMFI Codes:")
print(list(fund_codes)[:20])

print("\nValidation Completed")


import pandas as pd

df = pd.read_csv("cleaned_mutual_fund_data.csv", low_memory=False)


df["amfi_code"] = (
    df["amfi_code"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(".00", "", regex=False)
    .str.strip()
)


fund_codes = set(
    df["amfi_code"][
        (~df["amfi_code"].isin(["nan", "Unknown", ""]))
    ]
)

print("Total AMFI Codes:", len(fund_codes))

print("\nSample AMFI Codes:")
print(list(fund_codes)[:20])

print("\nValidation Completed")


import pandas as pd

df = pd.read_csv("cleaned_mutual_fund_data.csv", low_memory=False)

# AMFI code cleaning
df["amfi_code"] = (
    df["amfi_code"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(".00", "", regex=False)
    .str.strip()
)

fund_master_codes = set(
    df["amfi_code"].dropna().unique()
)

nav_history_codes = set(
    df[df["nav"].notna()]["amfi_code"].dropna().unique()
)

missing_codes = fund_master_codes - nav_history_codes

print("=== AMFI VALIDATION REPORT ===")
print("Fund Master Codes:", len(fund_master_codes))
print("NAV History Codes:", len(nav_history_codes))
print("Missing Codes:", len(missing_codes))

if missing_codes:
    print("\nMissing Codes:")
    print(list(missing_codes))
else:
    print("\nAll AMFI Codes are present in NAV History")