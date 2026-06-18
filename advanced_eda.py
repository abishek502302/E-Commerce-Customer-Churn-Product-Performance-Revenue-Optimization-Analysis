import pandas as pd

df = pd.read_csv("ecommerce_master_dataset.csv")

print("\n========== CHURN BY MEMBERSHIP ==========")
print(
    pd.crosstab(
        df['membership_tier'],
        df['churned'],
        normalize='index'
    ) * 100
)

print("\n========== CHURN BY NEWSLETTER ==========")
print(
    pd.crosstab(
        df['newsletter_subscribed'],
        df['churned'],
        normalize='index'
    ) * 100
)

print("\n========== PAYMENT METHODS ==========")
print(
    df['payment_method']
    .value_counts()
)

print("\n========== DEVICE USAGE ==========")
print(
    df['device_used']
    .value_counts()
)

print("\n========== RETURN RATE ==========")
print(
    df['returned']
    .value_counts(normalize=True) * 100
)

print("\n========== AVERAGE DELIVERY DAYS ==========")
print(
    df['delivery_days'].mean()
)

print("\n========== CUSTOMER RATING ==========")
print(
    df['customer_rating'].mean()
)