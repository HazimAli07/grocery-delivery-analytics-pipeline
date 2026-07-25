# Grocery Delivery Analytics Pipeline

SYST52461 Big Data Storage and Analysis term project using Databricks, PySpark, Delta tables, the Bronze-Silver-Gold medallion architecture, exploratory analysis, and a native Databricks dashboard.

## Team

- Hazim Ali
- Mannan
- Maheshwar
- Sweta
- Omar Leopoldo
- Shreyansh Pankaj

## Scenario

FreshRoute is a fictional grocery delivery company operating 25 stores across five Ontario cities. The project generates six related and deliberately imperfect source tables, cleans them into validated Silver tables, and creates Gold tables for revenue, product, store, delivery, discount, and customer-retention analysis.

## Repository structure

```text
notebooks/
  01_bronze_generation.ipynb
  02_silver_processing.ipynb
  03_gold_eda.ipynb
  04_hazim_customer_integration_validation.ipynb
dashboard/
  dashboard_queries.sql
  DASHBOARD_BUILD.md
report/
  SYST52461_Term_Project_Report.pdf
  REPORT_SOURCE.md
docs/
  DATA_DICTIONARY.md
  TEAM_CONTRIBUTIONS.md
  SUBMISSION_CHECKLIST.md
data/
  preview_kpis.json
  preview_*.csv
```

## Run instructions

1. In Databricks, import the three pipeline notebooks and any owner-validation notebooks from `notebooks/`.
2. Attach a cluster that supports Unity Catalog and Delta tables.
3. Run the notebooks in numeric order without skipping cells.
4. After Gold passes, run `04_hazim_customer_integration_validation.ipynb` and confirm `HAZIM_CUSTOMER_VALIDATION_PASSED`.
5. Confirm the final assertion or validation message in every notebook.
6. Open Databricks SQL and run the statements in `dashboard/dashboard_queries.sql`.
7. Follow `dashboard/DASHBOARD_BUILD.md` to assemble and verify the native dashboard.
8. Export the finished report from `report/` and submit this repository URL: https://github.com/HazimAli07/grocery-delivery-analytics-pipeline

## Data relationships

- `customers.CustomerID -> orders.CustomerID`
- `stores.StoreID -> orders.StoreID`
- `stores.StoreID -> products.StoreID`
- `orders.OrderID -> order_items.OrderID`
- `products.ProductID -> order_items.ProductID`
- `orders.OrderID -> deliveries.OrderID`

## Reproducibility and quality

All synthetic data uses seed `52461`. Bronze retains nulls, inconsistent labels, multiple date/percentage formats, invalid numeric values, duplicate keys, and orphan foreign keys. Silver applies column-specific rules and finishes with primary-key and foreign-key assertions. Gold calculations aggregate line items to the order grain before computing average order value.

## GitHub collaboration requirement

Every teammate must create a branch, make a meaningful improvement in the section they own, and open a pull request. Authorship comments do not replace commit history. See `docs/TEAM_CONTRIBUTIONS.md` for exact branch names and review assignments.
