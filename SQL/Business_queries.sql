USE sales_analysis;

-- 1. Overall KPIs
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    SUM(Sales) / COUNT(DISTINCT Order_ID) AS Average_Order_Value,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM cleaned_sales_data;

-- 2. Category Analysis
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Quantity_Sold
FROM cleaned_sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 3. Regional Analysis
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM cleaned_sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 4. Monthly Sales
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Sales_Month,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM cleaned_sales_data
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Sales_Month;

-- 5. Top Products
SELECT
    Product_Name,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Quantity_Sold
FROM cleaned_sales_data
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 6. Discount Analysis
SELECT
    Discount,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM cleaned_sales_data
GROUP BY Discount
ORDER BY Discount;

-- 7. Customer Analysis
SELECT
    Customer_ID,
    Customer_Name,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM cleaned_sales_data
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 8. Payment Method Analysis
SELECT
    Payment_Mode,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM cleaned_sales_data
GROUP BY Payment_Mode
ORDER BY Total_Sales DESC;

-- 9. Region + Category Analysis
SELECT
    Region,
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM cleaned_sales_data
GROUP BY Region, Category
ORDER BY Total_Sales DESC;


-- 10. Products with Sales Greater Than 10 Lakhs
SELECT
    Product_Name,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM cleaned_sales_data
GROUP BY Product_Name
HAVING SUM(Sales) > 1000000
ORDER BY Total_Sales DESC;


-- 11. Order Value Classification
SELECT
    Order_ID,
    Sales,
    CASE
        WHEN Sales >= 50000 THEN 'High Value'
        WHEN Sales >= 20000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Order_Value_Category
FROM cleaned_sales_data;


-- 12. Customer Sales Ranking
SELECT
    Customer_ID,
    Customer_Name,
    SUM(Sales) AS Total_Sales,
    RANK() OVER (ORDER BY SUM(Sales) DESC) AS Sales_Rank
FROM cleaned_sales_data
GROUP BY Customer_ID, Customer_Name;


-- 13. Top Product in Each Region
WITH ProductRegionSales AS (
    SELECT
        Region,
        Product_Name,
        SUM(Sales) AS Total_Sales
    FROM cleaned_sales_data
    GROUP BY Region, Product_Name
),
RankedProducts AS (
    SELECT
        Region,
        Product_Name,
        Total_Sales,
        RANK() OVER (
            PARTITION BY Region
            ORDER BY Total_Sales DESC
        ) AS Product_Rank
    FROM ProductRegionSales
)
SELECT
    Region,
    Product_Name,
    Total_Sales,
    Product_Rank
FROM RankedProducts
WHERE Product_Rank = 1
ORDER BY Region;


-- 14. Month-over-Month Sales Growth
WITH MonthlySales AS (
    SELECT
        DATE_FORMAT(Order_Date, '%Y-%m') AS Sales_Month,
        SUM(Sales) AS Total_Sales
    FROM cleaned_sales_data
    GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
),

MonthlyGrowth AS (
    SELECT
        Sales_Month,
        Total_Sales,
        LAG(Total_Sales) OVER (
            ORDER BY Sales_Month
        ) AS Previous_Month_Sales
    FROM MonthlySales
)

SELECT
    Sales_Month,
    Total_Sales,
    Previous_Month_Sales,
    CASE
        WHEN Previous_Month_Sales IS NULL THEN NULL
        ELSE
            ((Total_Sales - Previous_Month_Sales)
            / Previous_Month_Sales) * 100
    END AS MoM_Growth_Percentage
FROM MonthlyGrowth
ORDER BY Sales_Month;