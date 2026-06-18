import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset\product_summary.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove extra spaces from text columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# Standardize category names
if 'category' in df.columns:
    df['category'] = df['category'].str.title()

# Remove negative values from numeric columns
numeric_cols = [
    'total_orders',
    'total_revenue',
    'avg_price',
    'avg_rating',
    'return_rate',
    'avg_discount',
    'avg_delivery_days'
]

for col in numeric_cols:
    if col in df.columns:
        df = df[df[col] >= 0]

# Fix rating values (should be between 0 and 5)
if 'avg_rating' in df.columns:
    df = df[(df['avg_rating'] >= 0) & (df['avg_rating'] <= 5)]

# Fix return rate (should be between 0 and 100)
if 'return_rate' in df.columns:
    df = df[(df['return_rate'] >= 0) & (df['return_rate'] <= 100)]

# Create Revenue Per Order
if {'total_revenue', 'total_orders'}.issubset(df.columns):
    df['revenue_per_order'] = (
        df['total_revenue'] / df['total_orders']
    )
    df['revenue_per_order'] = df['revenue_per_order'].replace(
        [np.inf, -np.inf], 0
    )
    df['revenue_per_order'] = df['revenue_per_order'].fillna(0)

# Create Return Impact Score
if {'return_rate', 'total_revenue'}.issubset(df.columns):
    df['return_impact'] = (
        df['return_rate'] * df['total_revenue']
    ) / 100

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
df.to_csv("product_summary_cleaned.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("✅ Cleaned file saved as: product_summary_cleaned.csv")