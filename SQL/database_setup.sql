CREATE DATABASE sales_analysis;

CREATE TABLE sales_data (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Customer_Name VARCHAR(100),
    Region VARCHAR(20),
    State VARCHAR(50),
    City VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Discount DECIMAL(5,2),
    Sales DECIMAL(14,2),
    Profit DECIMAL(14,2),
    Payment_Mode VARCHAR(50)
);


-- Import your cleaned CSV
-- Choose cleaned_sales_data.csv
-- Select the sales_analysis database
-- Import into sales_data

USE sales_analysis;