import pandas as pd

# Load raw data
df = pd.read_csv("raw_data.csv")

df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Handle missing values
df.fillna({"name": "Unknown", "age": df["age"].median(), "purchase_amount": 0}, inplace=True)

# Convert purchase date to uniform format
df["purchasedate"] = pd.to_datetime(df["purchasedate"], errors="coerce")

df.to_json("final_data.csv", index=False)