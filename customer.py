import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset\customers.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert registration date to datetime
if 'registration_date' in df.columns:
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')

# Fill missing values
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove extra spaces from text columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# Standardize gender values
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.title()

# Remove unrealistic ages
if 'age' in df.columns:
    df = df[(df['age'] >= 18) & (df['age'] <= 80)]

# Create Customer Value
if {'total_orders', 'avg_order_value'}.issubset(df.columns):
    df['customer_value'] = df['total_orders'] * df['avg_order_value']

# Create Return Rate
if {'returns_made', 'total_orders'}.issubset(df.columns):
    df['return_rate'] = df['returns_made'] / df['total_orders']
    df['return_rate'] = df['return_rate'].replace([np.inf, -np.inf], 0)
    df['return_rate'] = df['return_rate'].fillna(0)

# Convert churned to category
if 'churned' in df.columns:
    df['churned'] = df['churned'].astype('category')

# Final checks
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nData Types:\n")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("customers_cleaned.csv", index=False)

print("\n✅ Data cleaning completed successfully!")
print("✅ Cleaned file saved as: customers_cleaned.csv")