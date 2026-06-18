import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("ecommerce_master_dataset.csv")

# 1 Revenue by Category
plt.figure(figsize=(10,5))
df.groupby('category')['total_amount_usd'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig("charts/revenue_by_category.png")
plt.close()

# 2 Revenue by Membership Tier
plt.figure(figsize=(6,4))
df.groupby('membership_tier')['total_amount_usd'].sum().plot(kind='bar')
plt.title("Revenue by Membership Tier")
plt.tight_layout()
plt.savefig("charts/revenue_by_membership_tier.png")
plt.close()

# 3 Top 10 Products
plt.figure(figsize=(12,5))
df.groupby('product_name')['total_amount_usd'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Products")
plt.tight_layout()
plt.savefig("charts/top_10_products.png")
plt.close()

# 4 Revenue by Country
plt.figure(figsize=(12,5))
df.groupby('country')['total_amount_usd'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Revenue by Country")
plt.tight_layout()
plt.savefig("charts/revenue_by_country.png")
plt.close()

# 5 Churn Distribution
plt.figure(figsize=(5,5))
df['churned'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Churn Distribution")
plt.ylabel("")
plt.savefig("charts/churn_distribution.png")
plt.close()

# 6 Device Usage
plt.figure(figsize=(6,4))
df['device_used'].value_counts().plot(kind='bar')
plt.title("Device Usage")
plt.tight_layout()
plt.savefig("charts/device_usage.png")
plt.close()

print("All charts saved in 'charts' folder")