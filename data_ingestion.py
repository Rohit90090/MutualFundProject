import pandas as pd
import os

folder_path = r"C:\Users\dell\Downloads"

files = os.listdir(folder_path)

dfs = []

for file in files:
    file_path = os.path.join(folder_path, file)

    try:
        if file.endswith(".csv"):
            df = pd.read_csv(file_path)
            dfs.append(df)
            print("Loaded:", file)

        elif file.endswith(".xlsx"):
            df = pd.read_excel(file_path)
            dfs.append(df)
            print("Loaded:", file)

    except Exception as e:
        print("Error:", file, e)

print("Total files loaded:", len(dfs))




final_df = pd.concat(dfs, ignore_index=True)

# merge 
print("\nMerged Shape:", final_df.shape)
print(final_df.head())

final_df.info()
final_df.isnull().sum().sort_values(ascending=False).head(10)
final_df.describe()
final_df['fund_house'].value_counts().head(10)
import matplotlib.pyplot as plt

final_df['fund_house'].value_counts().head(10).plot(kind='bar')
plt.title("Top Fund Houses")
plt.show()


print(final_df.shape)
print(final_df.columns)
final_df.isnull().sum().sort_values(ascending=False).head(10)
final_df['fund_house'].value_counts().head(10)
print("SCRIPT COMPLETED SUCCESSFULLY")
final_df.to_csv("data/processed/final_dataset.csv", index=False)
print("Saved final dataset successfully")