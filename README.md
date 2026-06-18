# E-Commerce Customer Churn, Product Performance & Revenue Optimization Analysis

## Project Overview

This project analyzes e-commerce business data to understand customer behavior, product performance, revenue trends, and customer churn. The objective is to identify key business metrics, monitor revenue growth, evaluate product performance, and support data-driven decision-making through interactive dashboards.

---

## Business Problem

E-commerce businesses generate large volumes of customer, order, and product data. However, without proper analysis, it is difficult to:

* Understand customer purchasing behavior
* Identify customer churn patterns
* Evaluate product performance
* Monitor revenue growth trends
* Improve customer retention strategies
* Optimize overall business performance

This project addresses these challenges through data analytics and visualization.

---

## Project Objectives

* Analyze customer purchasing behavior
* Measure customer churn rate
* Identify high-performing products and categories
* Analyze revenue trends over time
* Evaluate customer segmentation
* Build interactive Power BI dashboards
* Support business decision-making using data

---

## Dataset Information

### 1. customers_cleaned.csv

Contains customer-related information:

* Customer ID
* Country
* Age
* Gender
* Membership Tier
* Registration Date
* Total Orders
* Total Spend
* Average Order Value
* Days Since Last Purchase
* Preferred Category
* Preferred Device
* Preferred Payment Method
* Newsletter Subscription
* Customer Churn Status

---

### 2. orders_cleaned.csv

Contains order transaction details:

* Order ID
* Customer ID
* Order Date
* Product Name
* Category
* Quantity
* Unit Price
* Total Amount
* Payment Method
* Device Used
* Delivery Days
* Order Status
* Return Status
* Customer Rating

---

### 3. product_summary_cleaned.csv

Contains aggregated product information:

* Product Name
* Category
* Total Orders
* Total Revenue
* Average Price
* Average Rating
* Return Rate
* Average Discount
* Average Delivery Days

---

### 4. monthly_revenue_cleaned.csv

Contains monthly revenue performance:

* Year
* Month
* Quarter
* Orders
* Revenue
* Average Order Value
* Revenue Growth %
* Customer Growth %
* Revenue Per Customer

---

## Data Analytics Lifecycle

### 1. Data Collection

Collected four datasets:

* Customer Dataset
* Orders Dataset
* Product Summary Dataset
* Monthly Revenue Dataset

---

### 2. Data Cleaning

Performed:

* Missing value handling
* Data type correction
* Duplicate removal
* Feature engineering
* Return rate calculation
* Date formatting

---

### 3. Data Merging

Merged:

* customers_cleaned.csv
* orders_cleaned.csv
* product_summary_cleaned.csv

Generated:

```text
ecommerce_master_dataset.csv
```

Dimensions:

```text
25,000 rows × 56 columns
```

Monthly revenue dataset was kept separate:

```text
monthly_revenue_cleaned.csv
```

---

### 4. Exploratory Data Analysis (EDA)

Performed analysis on:

#### Customer Analysis

* Total Customers
* Churn Rate
* Membership Tier Distribution
* Newsletter Subscription Analysis

#### Revenue Analysis

* Total Revenue
* Revenue by Country
* Revenue by Membership Tier
* Revenue Trends

#### Product Analysis

* Revenue by Category
* Top Performing Products
* Return Rate Analysis

#### Operational Analysis

* Device Usage
* Payment Method Usage
* Average Delivery Time
* Customer Ratings

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib

### Data Visualization

* Power BI

### Development Environment

* Visual Studio Code

---

## Project Structure

```text
E-Commerce Customer Churn, Product Performance & Revenue Optimization Analysis

│
├── customers_cleaned.csv
├── orders_cleaned.csv
├── product_summary_cleaned.csv
├── monthly_revenue_cleaned.csv
│
├── ecommerce_master_dataset.csv
│
├── customer.py
├── orders.py
├── monthly.py
├── merge.py
├── ecom.py
├── eda_master.py
├── advanced_eda.py
├── revenue_analysis.py
│
├── charts/
├── revenue_charts/
│
├── PowerBI Dashboard.pbix
│
└── README.md
```

---

## Dashboard Pages

### Dashboard 1: Executive Summary

KPIs:

* Total Revenue
* Total Customers
* Total Orders
* Churn Rate

Visuals:

* Revenue by Category

---

### Dashboard 2: Customer Analysis

Visuals:

* Revenue by Membership Tier
* Churn by Membership Tier
* Revenue by Country
* Device Usage Distribution

---

### Dashboard 3: Product Analysis

Visuals:

* Revenue by Category
* Top 10 Products
* Return Rate by Category

---

## Key Metrics Calculated

### Churn Rate

```text
(Number of Churned Customers / Total Customers) × 100
```

### Return Rate

```text
(Returned Orders / Total Orders) × 100
```

### Revenue Growth %

```text
(Current Revenue - Previous Revenue) / Previous Revenue × 100
```

### Customer Growth %

```text
(Current Customers - Previous Customers) / Previous Customers × 100
```

### Dashboard Insights

### Page 1: Overall Business Performance
1. Strong Revenue Generation
Total revenue reached $3.14M from 25K orders and 7,663 customers.
Average revenue per customer is approximately $410, indicating good customer spending.
2. Electronics Dominates Sales
Electronics contributes more than 35% of total revenue (~$1.15M).
Revenue from Electronics is more than double that of the next category.
3. Revenue Concentration Risk
Top 3 categories (Electronics, Clothing & Apparel, Home & Kitchen) generate the majority of revenue.
Business is highly dependent on a few categories.
4. Churn Rate Concern
Overall churn rate is 8.9%.
Nearly 1 out of every 11 customers stops purchasing.
### Page 2: Customer & Geographic Analysis
5. United States Drives Revenue
The United States generates the highest revenue (~$1M).
It significantly outperforms all other countries.
6. International Markets Have Growth Potential
United Kingdom, India, Germany, and France are the next strongest markets.
Revenue drops sharply after the top countries.
7. Mobile Shopping Dominates
56% of customers use Mobile devices.
Desktop contributes around 32%.
Tablet usage is relatively low (~12%).
8. Gold Members Have Highest Churn
Gold members show the highest churn rate (~10%).
Silver and Platinum members have lower churn rates.
Premium customers may not be receiving enough value.
### Page 3: Product & Return Analysis
9. Best-Selling Products

Top revenue-generating products:

Portable Charger 20000mAh
Webcam 4K
Smart Watch Series 5
USB-C Hub
Wireless Earbuds Pro

Most top-selling products belong to the Electronics category.

10. Electronics Category Leads Revenue
Electronics significantly outperforms every other category.
Confirms strong demand for technology products.
11. High Return Rates in Certain Categories

Highest return rates:

Pet Supplies (~9.3%)
Travel & Luggage (~9.2%)
Home & Kitchen (~8.8%)
Food & Grocery (~8.5%)

These categories may have quality, sizing, expectation, or delivery issues.

12. Clothing & Apparel Has Lowest Return Rate
Lowest return rate among all categories.
Indicates better product-market fit and customer satisfaction.

### Recommendations

### Revenue Growth
1. Expand Electronics Portfolio
Increase inventory for top-selling electronics.
Introduce complementary products and bundles.
Focus marketing budget on high-performing tech products.
2. Reduce Dependence on One Category
Electronics contributes a very large share of revenue.
Strengthen Home & Kitchen and Clothing categories to diversify revenue streams.
Customer Retention
3. Investigate Gold Member Churn
Conduct surveys and feedback collection.
Offer exclusive rewards and loyalty benefits.
Review whether competitors offer better membership value.
4. Launch Retention Campaigns
Target customers inactive for 30–60 days.
Provide personalized offers and discounts.
Use email and app notifications for re-engagement.
Geographic Expansion
5. Focus on High-Potential Markets
Increase marketing efforts in:
United Kingdom
India
Germany
France
These markets already show strong demand.
6. Localize Marketing
Offer region-specific promotions and recommendations.
Optimize delivery and payment options for each country.
Mobile Experience
7. Prioritize Mobile Optimization
Since most customers use mobile devices:
Improve app performance.
Simplify checkout process.
Enhance mobile UI/UX.
Mobile improvements will impact the largest customer segment.
Return Reduction
8. Audit High-Return Categories

### Focus on:

Pet Supplies
Travel & Luggage
Home & Kitchen

### Actions:

Improve product descriptions.
Add better images and specifications.
Review supplier quality.
Analyze return reasons.
9. Promote Low-Return Categories
Increase visibility of Clothing & Apparel products.
Use them in cross-selling campaigns since they have lower return rates.
## Author

Abishek S.V 

Data Analytics Project


E-Commerce Customer Churn, Product Performance & Revenue Optimization Analysis
