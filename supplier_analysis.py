import pandas as pd
from sqlalchemy import create_engine

# CSV file path
file_path = "supply_chain_data.csv"

# Read CSV
df = pd.read_csv(file_path)

# Create delay & on-time columns
df['Delay_Days'] = df['Shipping times'] - df['Lead times']
df['On_Time'] = df['Delay_Days'].apply(lambda x: 1 if x <= 0 else 0)

# Supplier summary
supplier_summary = df.groupby('Supplier name').agg(
    Total_Orders=('SKU', 'count'),
    On_Time_Orders=('On_Time', 'sum'),
    On_Time_Percent=('On_Time', lambda x: round(x.sum()/x.count()*100, 2)),
    Avg_Delay=('Delay_Days', 'mean'),
    Total_Cost=('Costs', 'sum')
).reset_index()
supplier_summary.to_csv("supplier_summary.csv", index=False)

# Routes / Transportation summary
route_summary = df.groupby(['Routes', 'Transportation modes']).agg(
    Total_Orders=('SKU', 'count'),
    Late_Orders=('On_Time', lambda x: (x == 0).sum()),
    Avg_Delay=('Delay_Days', 'mean')
).reset_index()
route_summary.to_csv("route_summary.csv", index=False)

# Product type summary
product_summary = df.groupby('Product type').agg(
    Total_Orders=('SKU', 'count'),
    Late_Orders=('On_Time', lambda x: (x == 0).sum()),
    Avg_Delay=('Delay_Days', 'mean')
).reset_index()
product_summary.to_csv("product_summary.csv", index=False)

print("Aggregated CSVs created for dashboard.")

# ------------------ MySQL Upload ------------------
# MySQL connection details
MYSQL_USER = "root"
MYSQL_PASS = "Pavan@2018"   # 🔹 replace with your MySQL root password
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
DBNAME = "supply_chain"

# Create connection engine
engine = create_engine("mysql+pymysql://root:Pavan%402018@localhost:3306/supply_chain")


# Upload DataFrames to MySQL
supplier_summary.to_sql('supplier_summary', engine, if_exists='replace', index=False)
route_summary.to_sql('route_summary', engine, if_exists='replace', index=False)
product_summary.to_sql('product_summary', engine, if_exists='replace', index=False)

print("Uploaded summaries to MySQL: supplier_summary, route_summary, product_summary")
