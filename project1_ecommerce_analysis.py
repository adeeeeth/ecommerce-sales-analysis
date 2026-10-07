import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# PROJECT 1: E-COMMERCE SALES ANALYSIS
# Using the provided SuperStoreOrders.csv
# ==========================================

CSV_PATH = "SuperStoreOrders.csv"

# -----------------------------
# 1. LOAD DATA
# -----------------------------

df = pd.read_csv(CSV_PATH)

print("\n====================================")
print("DATASET INFORMATION")
print("====================================")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 2. DATA CLEANING
# -----------------------------

df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="mixed"
)

df["ship_date"] = pd.to_datetime(
    df["ship_date"],
    format="mixed"
)

df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["discount"] = pd.to_numeric(df["discount"], errors="coerce")
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")
df["shipping_cost"] = pd.to_numeric(df["shipping_cost"], errors="coerce")

df = df.dropna(
    subset=[
        "sales",
        "quantity",
        "profit",
        "order_date",
        "ship_date"
    ]
)

# Delivery time
df["delivery_days"] = (
    df["ship_date"] - df["order_date"]
).dt.days

print("\nMissing values:")
print(df.isnull().sum())

# ==========================================
# SECTION A — BASIC KPIs
# ==========================================

print("\n====================================")
print("SECTION A — BASIC KPIs")
print("====================================")

# Q1
total_revenue = df["sales"].sum()
print("\nQ1 Total Revenue:", total_revenue)

# Q2
total_profit = df["profit"].sum()
print("Q2 Total Profit:", total_profit)

# Q3
unique_customers = df["customer_name"].nunique()
print("Q3 Unique Customers:", unique_customers)

# Q4
total_quantity = df["quantity"].sum()
print("Q4 Total Quantity Sold:", total_quantity)

# Q5
# Dataset does not contain a separate Price column.
# We calculate average selling price per unit.
average_price = df["sales"].sum() / df["quantity"].sum()
print("Q5 Average Selling Price per Unit:", average_price)

# ==========================================
# SECTION B — CATEGORY & PRODUCT
# ==========================================

print("\n====================================")
print("SECTION B — CATEGORY & PRODUCT")
print("====================================")

# Q6
top_products = (
    df.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nQ6 Top 5 Best-Selling Products:")
print(top_products)

# Q7
category_revenue = (
    df.groupby("category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQ7 Revenue by Category:")
print(category_revenue)

print(
    "Highest Revenue Category:",
    category_revenue.idxmax()
)

# Q8
category_profit = df.groupby("category")[["sales", "profit"]].sum()

category_profit["profit_margin"] = (
    category_profit["profit"] /
    category_profit["sales"]
) * 100

print("\nQ8 Profit Margin by Category:")
print(category_profit["profit_margin"])

print(
    "Lowest Profit Margin Category:",
    category_profit["profit_margin"].idxmin()
)

# Q9
unique_products_category = (
    df.groupby("category")["product_name"]
    .nunique()
)

print("\nQ9 Unique Products per Category:")
print(unique_products_category)

# Q10
product_profit = (
    df.groupby("product_name")["profit"]
    .sum()
    .sort_values()
)

print("\nQ10 Product with Highest Total Loss:")
print(product_profit.head(1))

# ==========================================
# SECTION C — TIME SERIES & LOGISTICS
# ==========================================

print("\n====================================")
print("SECTION C — TIME SERIES & LOGISTICS")
print("====================================")

# Q11
monthly_sales = (
    df.set_index("order_date")["sales"]
    .resample("ME")
    .sum()
)

print("\nQ11 Highest Sales Month:")
print(monthly_sales.idxmax())
print("Sales:", monthly_sales.max())

# Q12
monthly_growth = monthly_sales.pct_change() * 100

print("\nQ12 Monthly Growth Rate:")
print(monthly_growth.dropna())

# Q13
weekday_orders = (
    df["order_date"]
    .dt.day_name()
    .value_counts()
)

print("\nQ13 Busiest Day of the Week:")
print(weekday_orders)

print(
    "Busiest Day:",
    weekday_orders.idxmax()
)

# Q14
average_delivery = df["delivery_days"].mean()

print("\nQ14 Average Delivery Time:")
print(round(average_delivery, 2), "days")

# Q15
df["quarter"] = df["order_date"].dt.quarter

q1_revenue = df[df["quarter"] == 1]["sales"].sum()
q4_revenue = df[df["quarter"] == 4]["sales"].sum()

print("\nQ15 Q4 vs Q1 Revenue")
print("Q1 Revenue:", q1_revenue)
print("Q4 Revenue:", q4_revenue)

if q4_revenue > q1_revenue:
    print("Q4 OUTPERFORMED Q1")
else:
    print("Q4 DID NOT OUTPERFORM Q1")

# ==========================================
# SECTION D — REGIONAL & CUSTOMER
# ==========================================

print("\n====================================")
print("SECTION D — REGIONAL & CUSTOMER")
print("====================================")

# Q16
region_sales = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQ16 Revenue by Region:")
print(region_sales)

print(
    "Best Region:",
    region_sales.idxmax()
)

# Q17
city_customers = (
    df.groupby("state")["customer_name"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\nQ17 Top 10 States by Unique Customers:")
print(city_customers)

# Q18
aov_region = (
    df.groupby("region")["sales"]
    .mean()
    .sort_values(ascending=False)
)

print("\nQ18 Average Order Value by Region:")
print(aov_region)

# Q19
# The provided dataset does NOT contain a Payment column.
print("\nQ19 Online vs COD:")
print("Cannot calculate because the provided dataset has no payment-method column.")

# Q20
discount_region = (
    df.groupby("region")["discount"]
    .mean()
    .sort_values(ascending=False)
)

print("\nQ20 Average Discount by Region:")
print(discount_region)

print(
    "Highest Average Discount Region:",
    discount_region.idxmax()
)

# ==========================================
# SECTION E — ADVANCED BUSINESS LOGIC
# ==========================================

print("\n====================================")
print("SECTION E — ADVANCED BUSINESS LOGIC")
print("====================================")

# Q21
customer_orders = (
    df.groupby("customer_name")["order_id"]
    .nunique()
)

repeat_customers = (customer_orders > 1).sum()
one_time_customers = (customer_orders == 1).sum()
total_customers = len(customer_orders)

repeat_percentage = (
    repeat_customers / total_customers
) * 100

one_time_percentage = (
    one_time_customers / total_customers
) * 100

print("\nQ21 Customer Purchase Behaviour")
print("Repeat Buyers:", round(repeat_percentage, 2), "%")
print("One-Time Buyers:", round(one_time_percentage, 2), "%")

# Q22
discount_profit_corr = df[
    ["discount", "profit"]
].corr().loc["discount", "profit"]

print("\nQ22 Discount vs Profit Correlation:")
print(discount_profit_corr)

# Q23
delivery_by_ship_mode = (
    df.groupby("ship_mode")["delivery_days"]
    .mean()
    .sort_values()
)

print("\nQ23 Average Delivery Time by Shipping Mode:")
print(delivery_by_ship_mode)

print(
    "Fastest Shipping Mode:",
    delivery_by_ship_mode.idxmin()
)

# Q24
sales_threshold = df["sales"].quantile(0.90)

high_sales_negative_profit = df[
    (df["sales"] >= sales_threshold) &
    (df["profit"] < 0)
]

print("\nQ24 High Sales but Negative Profit")
print(
    "Number of transactions:",
    len(high_sales_negative_profit)
)

# Top products in this segment
if len(high_sales_negative_profit) > 0:
    print("\nProducts causing high-sales losses:")
    print(
        high_sales_negative_profit
        .groupby("product_name")["profit"]
        .sum()
        .sort_values()
        .head(10)
    )

# Q25
regional_monthly = (
    df.set_index("order_date")
    .groupby("region")["sales"]
    .resample("ME")
    .sum()
    .reset_index()
)

regional_monthly["growth"] = (
    regional_monthly
    .groupby("region")["sales"]
    .pct_change()
)

growth_consistency = (
    regional_monthly
    .groupby("region")["growth"]
    .std()
    .sort_values()
)

print("\nQ25 Regional Growth Consistency:")
print(growth_consistency)

print(
    "Most Consistent Region:",
    growth_consistency.idxmin()
)

# ==========================================
# SAVE RESULTS
# ==========================================

results = {
    "Total Revenue": total_revenue,
    "Total Profit": total_profit,
    "Unique Customers": unique_customers,
    "Total Quantity Sold": total_quantity,
    "Average Selling Price per Unit": average_price,
    "Average Delivery Days": average_delivery,
    "Best Region": region_sales.idxmax(),
    "Highest Revenue Category": category_revenue.idxmax(),
    "Lowest Profit Margin Category": category_profit["profit_margin"].idxmin(),
    "Highest Discount Region": discount_region.idxmax(),
    "Repeat Buyers (%)": repeat_percentage,
    "One-Time Buyers (%)": one_time_percentage,
    "Discount-Profit Correlation": discount_profit_corr,
    "High Sales Negative Profit Transactions": len(
        high_sales_negative_profit
    ),
    "Fastest Shipping Mode": delivery_by_ship_mode.idxmin(),
    "Most Consistent Region": growth_consistency.idxmin()
}

results_df = pd.DataFrame(
    list(results.items()),
    columns=["Metric", "Value"]
)

results_df.to_csv(
    "project1_real_results.csv",
    index=False
)

print("\n====================================")
print("RESULTS SAVED")
print("====================================")
print(results_df)

# ==========================================
# VISUALIZATIONS
# ==========================================

sns.set_theme(style="whitegrid")

# 1. Revenue by Region
plt.figure(figsize=(9, 5))
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Monthly Revenue
plt.figure(figsize=(11, 5))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# 3. Category Revenue
plt.figure(figsize=(9, 5))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 4. Discount vs Profit
plt.figure(figsize=(9, 5))

sample = df.sample(
    min(5000, len(df)),
    random_state=42
)

sns.scatterplot(
    data=sample,
    x="discount",
    y="profit",
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

print("\nPROJECT 1 COMPLETED SUCCESSFULLY!")