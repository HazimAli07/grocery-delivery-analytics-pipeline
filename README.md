# Grocery Delivery Analytics Pipeline

SYST52461 Big Data Storage and Analysis term project built with Databricks, PySpark, Delta tables, the Bronze-Silver-Gold medallion architecture, exploratory analysis, and a native Databricks dashboard.

## Project at a glance

- **Scenario:** FreshRoute, a fictional grocery-delivery company operating 25 stores across five Ontario cities.
- **Databricks location:** catalog `workspace`, schema `analytics`.
- **Reproducible source data:** six related synthetic tables generated with seed `52461`.
- **Published dashboard:** [FreshRoute Grocery Delivery Performance](https://dbc-c58ab985-c7cd.cloud.databricks.com/dashboardsv3/01f187bb678d15ae91676a0d5422a14e?o=7474657090248704).
- **Final report:** [`report/SYST52461_Term_Project_Report.pdf`](report/SYST52461_Term_Project_Report.pdf), exactly five letter-size pages.

## Team and ownership

| Member | GitHub account | Primary ownership |
|---|---|---|
| Hazim Ali | [`HazimAli07`](https://github.com/HazimAli07) | Customers and final integration |
| Mannan | [`Mannan1398`](https://github.com/Mannan1398) | Store performance |
| Maheshwar | [`maheshwartandon`](https://github.com/maheshwartandon) | Product and category performance |
| Sweta | [`shwetachd1`](https://github.com/shwetachd1) | Order and monthly trends |
| Omar Leopoldo | [`OmarLeoR`](https://github.com/OmarLeoR) | Discount and revenue analysis |
| Shreyansh Pankaj | [`ShreyanshJoshi4444`](https://github.com/ShreyanshJoshi4444) | Delivery performance |

## Pipeline and notebook run order

1. `notebooks/01_bronze_generation.ipynb` creates deliberately imperfect Bronze Delta tables for customers, stores, products, orders, order items, and deliveries.
2. `notebooks/02_silver_processing.ipynb` parses, cleans, validates, deduplicates, and enforces primary-key and foreign-key integrity.
3. `notebooks/03_gold_eda.ipynb` produces analysis-ready sales-line, order, store, product, customer, monthly, category, discount, distance, loyalty, and executive-KPI tables.
4. Run the read-only owner validation notebooks `04` through `09` after Gold. Each reads the final tables and ends with a clearly named `*_VALIDATION_PASSED` marker. None of these notebooks writes or replaces tables.
5. Refresh the published dashboard datasets and confirm the KPI cards and global Month filter.

The three pipeline notebooks must be run in numeric order. The owner notebooks can then be run independently in any order.

## Verified Gold results

| KPI | Result |
|---|---:|
| Total net revenue | $172,835.74 |
| Completed orders | 3,636 |
| Average order value | $47.53 |
| On-time delivery rate | 27.14% |
| Repeat-customer rate | 83.32% |

The leading category is **Meat & Seafood** with 2,710 units, $50,649.02 net revenue, and $15,531.76 gross profit. The leading store is **FreshRoute Oakville 1** with 171 completed orders, 154 unique customers, and $9,477.16 net revenue.

## Data relationships

- `customers.CustomerID -> orders.CustomerID`
- `stores.StoreID -> orders.StoreID`
- `stores.StoreID -> products.StoreID`
- `orders.OrderID -> order_items.OrderID`
- `products.ProductID -> order_items.ProductID`
- `orders.OrderID -> deliveries.OrderID`

## Repository structure

```text
notebooks/   3 pipeline notebooks and 6 read-only owner validations
dashboard/   Databricks SQL queries and dashboard build/verification guide
report/      final five-page PDF, report source notes, and chart assets
docs/        data dictionary, contribution record, reviews, and checklist
data/        reproducible preview tables matching the verified Gold output
```

All six teammates contributed through their own GitHub accounts. The merged pull requests and final integration record are documented in [`docs/TEAM_CONTRIBUTIONS.md`](docs/TEAM_CONTRIBUTIONS.md).
