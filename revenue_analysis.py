import pandas as pd

revenue = pd.read_csv("monthly_revenue_cleaned.csv")

print("Total Revenue")
print(revenue['revenue_usd'].sum())

print("\nBest Revenue Month")
print(revenue.loc[revenue['revenue_usd'].idxmax()])

print("\nWorst Revenue Month")
print(revenue.loc[revenue['revenue_usd'].idxmin()])

print("\nAverage Revenue")
print(revenue['revenue_usd'].mean())

print("\nRevenue Growth")
print(revenue[['year','month','revenue_growth_pct']])