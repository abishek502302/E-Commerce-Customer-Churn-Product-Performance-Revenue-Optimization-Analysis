import pandas as pd
import matplotlib.pyplot as plt
import os

# Create separate folder
os.makedirs("revenue_charts", exist_ok=True)

revenue = pd.read_csv("monthly_revenue_cleaned.csv")

# Create date column
revenue['date'] = revenue['year'].astype(str) + '-' + revenue['month'].astype(str)

# 1. Monthly Revenue Trend
plt.figure(figsize=(12,5))
plt.plot(revenue['date'], revenue['revenue_usd'])
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("revenue_charts/monthly_revenue_trend.png")
plt.close()

# 2. Revenue Growth %
plt.figure(figsize=(12,5))
plt.plot(revenue['date'], revenue['revenue_growth_pct'])
plt.title("Revenue Growth %")
plt.xlabel("Month")
plt.ylabel("Growth %")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("revenue_charts/revenue_growth.png")
plt.close()

# 3. Customer Growth %
plt.figure(figsize=(12,5))
plt.plot(revenue['date'], revenue['customer_growth_pct'])
plt.title("Customer Growth %")
plt.xlabel("Month")
plt.ylabel("Growth %")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("revenue_charts/customer_growth.png")
plt.close()

# 4. Quarterly Revenue
plt.figure(figsize=(8,5))
revenue.groupby('quarter')['revenue_usd'].sum().plot(kind='bar')
plt.title("Quarterly Revenue")
plt.xlabel("Quarter")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_charts/quarterly_revenue.png")
plt.close()

# 5. Revenue Per Customer
plt.figure(figsize=(12,5))
plt.plot(revenue['date'], revenue['revenue_per_customer'])
plt.title("Revenue Per Customer")
plt.xlabel("Month")
plt.ylabel("Revenue Per Customer")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("revenue_charts/revenue_per_customer.png")
plt.close()

print("✅ All revenue charts saved in revenue_charts folder")