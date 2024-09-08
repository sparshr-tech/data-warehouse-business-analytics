import pandas as pd

# Load the dataset
df = pd.read_csv('C://Users//S//Documents//GitHub//data-warehouse-business-analytics//data//Online Retail.csv', encoding='ISO-8859-1')  # Make sure the path matches your file name

# Print the first few rows to inspect the data
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
#print("\nMissing values in each column:")
#print(df.isnull().sum())

# Dataframe shape
#print(f"\nThe dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Clean the data
# Drop rows where 'CustomerID' is missing
df_cleaned = df.dropna(subset=['CustomerID']).copy()  # Use .copy() to avoid SettingWithCopyWarning

# Fill missing 'Description' values with a placeholder
df_cleaned['Description'] = df_cleaned['Description'].fillna('Unknown Product')

# Convert 'InvoiceDate' to datetime format, using dayfirst=True to parse correctly
df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'], dayfirst=True, errors='coerce')

# Create a new 'TotalAmount' column (Quantity * UnitPrice)
df_cleaned['TotalAmount'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']

# Print cleaned data information
print(f"\nCleaned dataset contains {df_cleaned.shape[0]} rows and {df_cleaned.shape[1]} columns.")

# Show some cleaned rows and new 'TotalAmount'
#print("\nFirst 5 rows of the cleaned dataset with 'TotalAmount':")
#print(df_cleaned[['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'UnitPrice', 'TotalAmount', 'Country']].head())

# Checking missing values after cleaning
#print("\nMissing values in cleaned dataset:")
#print(df_cleaned.isnull().sum())

# Create Dimension Tables

# Dimension: Product (unique StockCode and Description)
dim_product = df_cleaned[['StockCode', 'Description']].drop_duplicates().reset_index(drop=True)
dim_product.to_csv('C://Users//S//Documents//GitHub//data-warehouse-business-analytics//data//dim_product.csv', index=False)

# Dimension: Customer (unique CustomerID and Country)
dim_customer = df_cleaned[['CustomerID', 'Country']].drop_duplicates().reset_index(drop=True)
dim_customer.to_csv('C://Users//S//Documents//GitHub//data-warehouse-business-analytics//data//dim_customer.csv', index=False)

# Dimension: Date (Extract year, month, day from InvoiceDate)
df_cleaned['Year'] = df_cleaned['InvoiceDate'].dt.year
df_cleaned['Month'] = df_cleaned['InvoiceDate'].dt.month
df_cleaned['Day'] = df_cleaned['InvoiceDate'].dt.day
dim_date = df_cleaned[['InvoiceDate', 'Year', 'Month', 'Day']].drop_duplicates().reset_index(drop=True)
dim_date.to_csv('C://Users//S//Documents//GitHub//data-warehouse-business-analytics//data//dim_date.csv', index=False)

# Fact Table: Sales
fact_sales = df_cleaned[['InvoiceNo', 'StockCode', 'CustomerID', 'Quantity', 'TotalAmount', 'InvoiceDate']]
fact_sales.to_csv('C://Users//S//Documents//GitHub//data-warehouse-business-analytics//data//fact_sales.csv', index=False)

print("Dimension and fact tables saved successfully.")