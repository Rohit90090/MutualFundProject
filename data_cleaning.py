import pandas as pd

df = pd.read_csv("data/processed/final_dataset.csv")

print(df.shape)
print(df.isnull().sum())

df = df.drop_duplicates()

num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaning Done")