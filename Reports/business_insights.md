# Sales Data Analysis & Business Insights

## 1. Project Objective

The objective of this project is to analyze sales data and identify
business trends related to sales, profit, products, customers,
regions, discounts, and payment methods.

The analysis was performed using Python, Pandas, SQL, and Power BI
to generate meaningful business insights and support data-driven
decision-making.



## 2. Dataset Description

This project uses a synthetic retail sales dataset created for
portfolio and learning purposes.

The dataset contains 10,020 raw records and 16 columns.

The dataset includes information about:

- Order details
- Customers
- Regions
- States
- Cities
- Product categories
- Products
- Quantity
- Unit price
- Discounts
- Sales
- Profit
- Payment methods

After data cleaning, 20 duplicate records were removed, resulting
in 10,000 final records for analysis.



## 3. Data Cleaning

Data cleaning was performed using Python and Pandas.

The following steps were performed:

- Converted Order_Date to datetime format.
- Removed duplicate records.
- Handled missing Customer_Name values.
- Handled missing City values.
- Handled missing Payment_Mode values.
- Checked numerical columns.
- Verified duplicate records after cleaning.
- Exported the cleaned dataset for SQL and Power BI analysis.

### Cleaning Results

- Initial records: 10,020
- Duplicate records removed: 20
- Final records: 10,000
- Missing values after cleaning: 0
- Duplicate records after cleaning: 0



## 4. Overall Business Performance

| KPI | Value |
|---|---:|
| Total Sales | ₹246.68M |
| Total Profit | ₹43.71M |
| Total Orders | 10,000 |
| Total Quantity Sold | 25,747 |
| Average Order Value | ₹24,667.60 |
| Profit Margin | 17.72% |

The dataset generated approximately ₹246.68M in total sales and
₹43.71M in total profit across 10,000 orders.

The overall profit margin was 17.72%, while the average order value
was approximately ₹24,667.60.



## 5. Category Analysis

Electronics was the highest-performing category.

It generated approximately ₹153.5M in sales and ₹27.1M in profit,
making it the largest contributor to overall business performance.

Electronics accounted for approximately 62% of total sales.

| Category | Sales | Profit |
|---|---:|---:|
| Electronics | ₹153.5M | ₹27.1M |
| Furniture | ₹51.6M | ₹9.3M |
| Office Supplies | ₹22.0M | ₹3.9M |
| Home Appliances | ₹19.6M | ₹3.5M |



## 6. Regional Analysis

The South region was the strongest-performing region.

| Region | Sales | Profit |
|---|---:|---:|
| South | ₹94.2M | ₹17.1M |
| North | ₹60.3M | ₹10.8M |
| West | ₹55.2M | ₹9.7M |
| East | ₹37.0M | ₹6.1M |

The South region generated the highest sales and profit among all
four regions.



## 7. Monthly Sales Analysis

May 2025 recorded the highest monthly sales at approximately
₹24.54M.

February 2025 recorded the lowest monthly sales at approximately
₹17.28M.

The monthly analysis shows variation in sales performance throughout
2025.

Since the dataset covers only one year, the results should be
considered observed monthly variation rather than confirmed
long-term seasonality.



## 8. Product Analysis

ApexBook 14 was the leading product by sales.

It generated approximately ₹95.1M in sales and ₹16.9M in profit.

Other high-performing products included Nova X1, LaserJet Basic,
ViewPlus 24, and WorkDesk Pro.

| Product | Sales |
|---|---:|
| ApexBook 14 | ₹95.1M |
| Nova X1 | ₹33.0M |
| LaserJet Basic | ₹20.1M |
| ViewPlus 24 | ₹17.8M |
| WorkDesk Pro | ₹17.3M |



## 9. Discount Analysis

The analysis showed an association between higher discount levels and
lower profit margins.

Profit margin decreased from approximately 24.14% at 0% discount to
approximately 6.89% at 20% discount.

This suggests that discount strategies should be evaluated not only
for their impact on sales but also for their impact on profitability.

This analysis identifies an association and does not prove that
discounts alone caused the reduction in profit margin.



## 10. Payment Method Analysis

UPI was the highest-performing payment method by sales and order
volume.

UPI generated approximately ₹81.9M in sales across 3,462 orders.

Credit Card was the second-highest payment method by sales.



## 11. Customer Analysis

Customer-level analysis was performed to identify customers with
high sales and profit contributions.

The analysis showed that the customer with the highest sales was not
necessarily the customer with the highest profit.

This demonstrates the importance of evaluating both revenue and
profitability when identifying high-value customers.



## 12. Business Recommendations

### 1. Focus on High-Performing Categories

Electronics is the strongest category by sales and profit.
Inventory and promotional strategies should prioritize
high-performing electronics products.

### 2. Analyze South Region Performance

The South region generates the highest sales and profit.
The factors behind its strong performance could be studied and
successful approaches considered for other regions.

### 3. Monitor Discount Strategies

Higher discounts are associated with lower profit margins.
Discount campaigns should therefore be evaluated based on both
revenue and profitability.

### 4. Monitor High-Performing Products

ApexBook 14 contributes significantly to total sales.
Its demand and inventory levels should be monitored carefully.

### 5. Evaluate Customers Using Profit as Well as Sales

Customer performance should be evaluated using sales, profit, and
order frequency rather than sales alone.



## 13. Tools & Technologies

- Python
- Pandas
- SQL
- MySQL
- Power BI
- Excel
- GitHub



