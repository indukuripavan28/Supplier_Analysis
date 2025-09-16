import pandas as pd

# Your CSV file path
file_path = "/Users/pavanindukuri/Desktop/Data Analysis/supply_chain_data.csv"

# Read CSV
df = pd.read_csv(file_path)

# Preview data
print("Rows, Columns:", df.shape)
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values per column:\n", df.isnull().sum())