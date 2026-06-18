import pandas as pd

customers = pd.read_csv("customers_cleaned.csv")
orders = pd.read_csv("orders_cleaned.csv")
products = pd.read_csv("product_summary_cleaned.csv")
revenue = pd.read_csv("monthly_revenue_cleaned.csv")

print("CUSTOMERS")
print(customers.columns.tolist())

print("\nORDERS")
print(orders.columns.tolist())

print("\nPRODUCTS")
print(products.columns.tolist())

print("\nREVENUE")
print(revenue.columns.tolist())