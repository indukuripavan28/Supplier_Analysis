# Supplier Analysis Dashboard

## Overview
This project performs data analysis on a supply chain dataset and generates interactive dashboards for supplier, route, and product insights. The analysis focuses on order performance, delays, and cost summaries, helping businesses make informed decisions.

## Features
- Aggregates and summarizes supply chain data by **Supplier**, **Route**, and **Product type**.
- Calculates key metrics:
  - Total Orders
  - On-Time Orders & Percentage
  - Average Delay in Shipping
  - Total Costs
- Uploads aggregated summaries to **MySQL** for central storage.
- Creates interactive dashboards using **Looker Studio / Power BI** with:
  - Bar charts, line charts, and KPI cards.
  - Filters and slicers for dynamic exploration.

## Project Structure

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/indukuripavan28/Supplier_Analysis.git
   cd Supplier_Analysis
python -m venv venv
source venv/bin/activate  # Mac/Linux

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # Mac/Linux

3. Install packages:
pip install pandas sqlalchemy pymysql openpyxl

4.Update MySQL credentials in supplier_analysis.py:
MYSQL_USER = "root"
MYSQL_PASS = "your_password"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
DBNAME = "supply_chain"

Usage
1.Explore the dataset:
python explore_data.py

2. Aggregate data and upload to MySQL:
python supplier_analysis.py

3.Open Looker Studio / Power BI:
 -Connect to aggregated CSVs or MySQL database.
 -Build interactive dashboards for supplier, route, and product summaries.
Insights
 -Quickly identify suppliers with high delays or low on-time performance.
 -Analyze cost and order distribution by supplier, route, and product.
 -Enable better supply chain decision-making through interactive visualization.

📊 Interactive Dashboard
Explore the interactive Supplier Analysis Dashboard created using Looker Studio:
👉 https://lookerstudio.google.com/u/0/reporting/74ee394e-2591-48cb-ae3d-41da10281bb5/page/1NKYF 
