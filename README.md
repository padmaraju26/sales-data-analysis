
# Sales Data Analysis & Business Insights

## 📊 Project Overview

This project analyzes retail sales data to identify trends and
business insights related to sales, profit, products, customers,
regions, discounts, and payment methods.

The project follows an end-to-end data analytics workflow using
Python, Pandas, SQL, MySQL, and Power BI.

## 🎯 Project Objective

The main objectives of this project are to:

- Clean and prepare sales data using Python and Pandas.
- Perform exploratory data analysis.
- Analyze sales and profitability using SQL.
- Identify high-performing products and categories.
- Analyze regional and monthly sales performance.
- Understand the relationship between discounts and profitability.
- Create an interactive Power BI dashboard.
- Generate actionable business insights.

## 📁 Dataset

This project uses a synthetic retail sales dataset created for
portfolio and learning purposes.

The raw dataset contains 10,020 records and 16 columns.

After data cleaning:

- 20 duplicate records were removed.
- Missing values were handled.
- 10,000 records remained for analysis.

The dataset contains information about:

- Orders
- Customers
- Regions
- Cities
- Product Categories
- Products
- Quantity
- Unit Price
- Discount
- Sales
- Profit
- Payment Method



## 🛠️ Tools & Technologies

- Python
- Pandas
- SQL
- MySQL
- Power BI
- Excel
- GitHub



## 🔄 Project Workflow

Raw Sales Data
       ↓
Data Cleaning with Python/Pandas
       ↓
Exploratory Data Analysis
       ↓
SQL Business Analysis
       ↓
Power BI Dashboard
       ↓
Business Insights
       ↓
Business Recommendations


## 📈 Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Sales | ₹246.68M |
| Total Profit | ₹43.71M |
| Total Orders | 10,000 |
| Total Quantity Sold | 25,747 |
| Average Order Value | ₹24,667.60 |
| Profit Margin | 17.72% |


## 🔍 Key Business Insights

- Electronics was the highest-performing category.
- South region generated the highest sales.
- ApexBook 14 was the leading product by sales.
- May 2025 recorded the highest monthly sales.
- UPI was the highest-volume payment method.
- Higher discount levels were associated with lower profit margins.
- Customer sales and customer profitability did not always produce
  the same ranking.


## 📊 Power BI Dashboard

The interactive Power BI dashboard provides an overview of sales
performance through KPIs, trends, regional analysis, category
analysis, and top-product performance.

![Sales Performance Dashboard](screenshots/dashboard.png)


## 🧮 SQL Analysis

SQL was used to perform business-focused analysis including:

- Overall sales and profit KPIs
- Category performance
- Regional performance
- Monthly sales trends
- Top products
- Discount analysis
- Customer analysis
- Payment method analysis
- Region and category analysis
- High-sales products using HAVING
- Order-value classification using CASE
- Customer ranking using RANK()
- Top products by region using CTE and window functions
- Month-over-month sales growth using LAG()


## 💡 Business Recommendations

1. Prioritize high-performing electronics products and monitor their
   inventory levels.

2. Analyze the factors contributing to strong South-region
   performance and evaluate opportunities in other regions.

3. Monitor discount strategies because higher discount levels were
   associated with lower profit margins.

4. Track high-performing products such as ApexBook 14 closely.

5. Evaluate customers using both sales and profit contribution
   rather than revenue alone.


## 📂 Project Structure

sales-data-analysis/
│
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
│
├── python/
│   ├── data_cleaning.py
│   └── sales_analysis.py
│
├── sql/
│   ├── database_setup.sql
│   └── business_queries.sql
│
├── powerbi/
│   └── Sales_Analysis_Dashboard.pbix
│
├── reports/
│   └── business_insights.md
│
├── screenshots/
│   └── dashboard.png
│
└── README.md


# sales-data-analysis
End-to-end sales data analysis using Python, SQL, and Power BI

