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