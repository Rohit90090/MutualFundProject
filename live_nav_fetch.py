import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Scheme Name:", data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv("data/raw/hdfc_top100_nav.csv", index=False)

print("Live NAV data saved successfully")


scheme_codes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(f"data/raw/{name}.csv", index=False)

    print(f"{name} NAV saved successfully")