
# Real-World Data Analytics Projects

These two projects are based directly on the uploaded `Python Data Analytics: 50 Business Case Studies` requirements.

## Project 1 — E-Commerce Sales Analysis
Goal: turn 1M+ transactional rows into revenue, profit, product, regional, customer, logistics and growth insights.

Tools from the requirements: Pandas, NumPy, Matplotlib and Seaborn.

Files:
- `project1_ecommerce_analysis.py`
- Expected real dataset: `amazon_sales.csv`

The script automatically creates a 1,000,000-row synthetic practice dataset if `amazon_sales.csv` is not present. This is only for learning/demo purposes and must not be presented as real Amazon data.

## Project 2 — Telecom Customer Churn Analysis
Goal: identify at-risk customers and retention factors to reduce revenue loss.

Tools from the requirements: Pandas, Matplotlib and Seaborn.

Files:
- `project2_telecom_churn.py`
- Expected real dataset: `telecom_churn.csv`

The script automatically creates a practice dataset if the real CSV is missing.

## How to run
1. Install Python 3.x.
2. Install packages:
   `pip install pandas numpy matplotlib seaborn`
3. Put the relevant CSV beside the script, OR let the script generate practice data.
4. Run:
   `python project1_ecommerce_analysis.py`
   `python project2_telecom_churn.py`

## Important dataset note
The uploaded requirements specify column names such as Sales, Profit, Customer ID, Quantity, Price, Order Date, Delivery, Region, City, Category, Product, Discount and Payment for Project 1; and Age, SeniorCitizen, Tenure, MonthlyCharges, Churn, Contract, InternetService, PaymentMethod, Dependents, OnlineSecurity, TechSupport, MultipleLines, PaperlessBilling and support-related fields for Project 2. Your actual CSV may use different names, so the loading section should be adjusted to match the dataset.

The uploaded requirements' Q31 asks for Male/Female churn, but the listed telecom fields do not include Gender. The provided script therefore explicitly reports that this cannot be calculated unless Gender is present in the real dataset.
