import pandas as pd

try:
    print("Loading dataset...")

    df = pd.read_csv("ecommerce_master_dataset.csv")

    print("Dataset Loaded Successfully!")
    print("Shape:", df.shape)

    print("\n========== TOTAL CUSTOMERS ==========")
    print(df['customer_id'].nunique())

    print("\n========== TOTAL ORDERS ==========")
    print(df['order_id'].nunique())

    print("\n========== TOTAL REVENUE ==========")
    print(round(df['total_amount_usd'].sum(), 2))

    print("\n========== CHURN RATE (%) ==========")
    print(df['churned'].value_counts(normalize=True) * 100)

    print("\n========== REVENUE BY CATEGORY ==========")
    print(
        df.groupby('category')['total_amount_usd']
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== REVENUE BY MEMBERSHIP TIER ==========")
    print(
        df.groupby('membership_tier')['total_amount_usd']
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== TOP 10 PRODUCTS ==========")
    print(
        df.groupby('product_name')['total_amount_usd']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========== REVENUE BY COUNTRY ==========")
    print(
        df.groupby('country')['total_amount_usd']
        .sum()
        .sort_values(ascending=False)
    )

except Exception as e:
    print("ERROR:", e)