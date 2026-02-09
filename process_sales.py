import pandas as pd

# List of input files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"].str.lower() == "pink morsel"]

    # Clean price column (remove $ and convert to float)
    df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

    # Ensure quantity numeric
    df["quantity"] = pd.to_numeric(df["quantity"])

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required fields
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

# Combine all files
final_df = pd.concat(dfs, ignore_index=True)

# Save output
final_df.to_csv("formatted_sales.csv", index=False)

print("Done! Output saved as formatted_sales.csv")
