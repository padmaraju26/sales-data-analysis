import pandas as pd

#------------------------------------------------------
# 1. load the sales data from a csv file
#------------------------------------------------------
df = pd.read_csv("../data/raw_sales_data.csv")
print(df)

print("Original dataset:")
print(df.head())

print("\nOriginal shape:")
print(df.shape)


#------------------------------------------------------
# 2. Convert Date
#------------------------------------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])


#------------------------------------------------------
# 3. Remove duplicates Rows
#------------------------------------------------------
print("\nBefore removing duplicates:", len(df))

df = df.drop_duplicates()

print("After removing duplicates:", len(df))


#------------------------------------------------------
# 4. Handle missing values
#------------------------------------------------------
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown Customer")
df["City"] = df["City"].fillna("Unknown City")
df["Payment_Mode"] = df["Payment_Mode"].fillna("Unknown")


#------------------------------------------------------
# 5. Validate cleaned data
#------------------------------------------------------
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nFinal shape:")
print(df.shape)


#------------------------------------------------------
# 6. saved cleaned  data to a new csv file
#------------------------------------------------------
df.to_csv("../data/cleaned_sales_data.csv", index=False)
print("\nCleaned data saved successfully to cleaned_sales_data.csv")


#------------------------------------------------------
# 7. Basic Business KPIs
#------------------------------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100


print("\n ============ Basic Business KPIs ============")

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")


#------------------------------------------------------
# 8. Categorical performance
#------------------------------------------------------
category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Quantity_Sold=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)
print("\n========== CATEGORY PERFORMANCE ==========")
print(category_analysis)


#------------------------------------------------------
# 9. Reginal performance
#------------------------------------------------------
region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Total_Sales", ascending=False)
print("\n========== REGIONAL PERFORMANCE ==========")
print(region_analysis)


#------------------------------------------------------
# 10. monthly sales trend
#------------------------------------------------------
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)
print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


#------------------------------------------------------
# 11. Top 10 Products by Sales
# ------------------------------------------------------
product_sales = df.groupby("Product_Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Quantity_Sold=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)
print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(product_sales.head(10))


# ------------------------------------------------------
# 12. Top 10 Products by Profit
# ------------------------------------------------------
product_profit = product_sales.sort_values(
    "Total_Profit",
    ascending=False
)
print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")
print(product_profit.head(10))


# ------------------------------------------------------
# 13. Loss-Making Products
# ------------------------------------------------------
loss_products = product_sales[
    product_sales["Total_Profit"] < 0
].sort_values("Total_Profit")
print("\n========== LOSS-MAKING PRODUCTS ==========")
print(loss_products)

# ------------------------------------------------------
# 14. Top 10 Customers by Sales
# ------------------------------------------------------
customer_analysis = df.groupby(
    ["Customer_ID", "Customer_Name"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Total_Sales", ascending=False)
print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
print(customer_analysis.head(10))


# ------------------------------------------------------
# 15. Top 10 Customers by Profit
# ------------------------------------------------------
customer_profit = customer_analysis.sort_values(
    "Total_Profit",
    ascending=False
)
print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")
print(customer_profit.head(10))


# ------------------------------------------------------
# 16. Product Profit Margin
# ------------------------------------------------------
product_analysis = df.groupby("Product_Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Quantity_Sold=("Quantity", "sum")
)

product_analysis["Profit_Margin"] = (
    product_analysis["Total_Profit"]
    / product_analysis["Total_Sales"]
) * 100

product_analysis = product_analysis.sort_values(
    "Profit_Margin",
    ascending=False
)

print("\n========== PRODUCTS BY PROFIT MARGIN ==========")
print(product_analysis)



# ------------------------------------------------------
# 17. Discount Analysis
# ------------------------------------------------------
discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
)

discount_analysis["Profit_Margin"] = (
    discount_analysis["Total_Profit"]
    / discount_analysis["Total_Sales"]
) * 100

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)


# ------------------------------------------------------
# 18. Payment Method Analysis
# ------------------------------------------------------
payment_analysis = df.groupby("Payment_Mode").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values(
    "Total_Sales",
    ascending=False
)

payment_analysis["Profit_Margin"] = (
    payment_analysis["Total_Profit"]
    / payment_analysis["Total_Sales"]
) * 100

print("\n========== PAYMENT METHOD ANALYSIS ==========")
print(payment_analysis)


# ------------------------------------------------------
# 19. Region + Category Analysis
# ------------------------------------------------------
region_category = df.groupby(
    ["Region", "Category"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values(
    "Total_Sales",
    ascending=False
)

print("\n========== REGION + CATEGORY ANALYSIS ==========")
print(region_category)