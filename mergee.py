import pandas as pd

customers = pd.read_csv("customers_cleaned.csv")
orders = pd.read_csv("orders_cleaned.csv")
products = pd.read_csv("product_summary_cleaned.csv")

# Merge customers and orders
customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

# Merge product information
master_data = pd.merge(
    customer_orders,
    products,
    on=["product_name", "category"],
    how="left"
)

print("Final Shape:", master_data.shape)

master_data.to_csv(
    "ecommerce_master_dataset.csv",
    index=False
)

print("✅ ecommerce_master_dataset.csv created successfully")