import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset/monthly_revenue.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing numeric values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove extra spaces
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip()

# Validate Year
if 'year' in df.columns:
    df = df[(df['year'] >= 2000) & (df['year'] <= 2100)]

# Validate Month
if 'month' in df.columns:
    df = df[(df['month'] >= 1) & (df['month'] <= 12)]

# Validate Revenue
if 'revenue_usd' in df.columns:
    df = df[df['revenue_usd'] >= 0]

# Validate Orders
if 'orders' in df.columns:
    df = df[df['orders'] >= 0]

# Validate Return Rate
if 'return_rate' in df.columns:
    df = df[(df['return_rate'] >= 0) & (df['return_rate'] <= 100)]

# Validate Discount
if 'avg_discount' in df.columns:
    df = df[(df['avg_discount'] >= 0) & (df['avg_discount'] <= 100)]

# Create Revenue Per Customer
if {'revenue_usd', 'unique_customers'}.issubset(df.columns):
    df['revenue_per_customer'] = (
        df['revenue_usd'] / df['unique_customers']
    )
    df['revenue_per_customer'] = df['revenue_per_customer'].replace(
        [np.inf, -np.inf], 0
    ).fillna(0)

# Create Revenue Growth %
df = df.sort_values(['year', 'month'])

if 'revenue_usd' in df.columns:
    df['revenue_growth_pct'] = (
        df['revenue_usd'].pct_change() * 100
    )
    df['revenue_growth_pct'] = df['revenue_growth_pct'].fillna(0)

# Create Customer Growth %
if 'unique_customers' in df.columns:
    df['customer_growth_pct'] = (
        df['unique_customers'].pct_change() * 100
    )
    df['customer_growth_pct'] = df['customer_growth_pct'].fillna(0)

# Final checks
print("Dataset Shape:", df.shape)

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:\n")
print(df.dtypes)

print("\nSummary Statistics:\n")
print(df.describe())

# Save cleaned dataset
df.to_csv("monthly_revenue_cleaned.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("✅ Cleaned file saved as: monthly_revenue_cleaned.csv")