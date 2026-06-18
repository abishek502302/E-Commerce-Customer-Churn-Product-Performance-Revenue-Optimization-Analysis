import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset\orders.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert order date
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Fill missing numeric values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove extra spaces
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip()

# Standardize text columns
text_cols = [
    'category',
    'payment_method',
    'device',
    'delivery_status',
    'day_of_week'
]

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.title()

# Remove negative values
numeric_cols = [
    'unit_price',
    'quantity',
    'subtotal',
    'discount',
    'discount_amount',
    'shipping_tax',
    'pct_tax',
    'tax_amount',
    'total_amount',
    'delivery_days',
    'customer_session_pages',
    'session_duration'
]

for col in numeric_cols:
    if col in df.columns:
        df = df[df[col] >= 0]

# Quantity validation
if 'quantity' in df.columns:
    df = df[df['quantity'] > 0]

# Discount validation
if 'discount' in df.columns:
    df = df[(df['discount'] >= 0) & (df['discount'] <= 100)]

# Tax validation
if 'pct_tax' in df.columns:
    df = df[(df['pct_tax'] >= 0) & (df['pct_tax'] <= 100)]

# Delivery days validation
if 'delivery_days' in df.columns:
    df = df[(df['delivery_days'] >= 0) & (df['delivery_days'] <= 60)]

# Create Revenue Per Unit
if {'total_amount', 'quantity'}.issubset(df.columns):
    df['revenue_per_unit'] = df['total_amount'] / df['quantity']
    df['revenue_per_unit'] = df['revenue_per_unit'].replace(
        [np.inf, -np.inf], 0
    )
    df['revenue_per_unit'] = df['revenue_per_unit'].fillna(0)

# Create Net Revenue
if {'total_amount', 'discount_amount'}.issubset(df.columns):
    df['net_revenue'] = (
        df['total_amount'] - df['discount_amount']
    )

# Create Return Flag
if 'returned' in df.columns:
    df['return_flag'] = df['returned'].astype(int)

# Final validation
print("Dataset Shape:", df.shape)

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:\n")
print(df.dtypes)

print("\nSummary Statistics:\n")
print(df.describe())

# Save cleaned dataset
df.to_csv("orders_cleaned.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("✅ Cleaned file saved as: orders_cleaned.csv")