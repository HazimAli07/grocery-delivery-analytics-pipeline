# Report Source Summary

The final five-page PDF is `SYST52461_Term_Project_Report.pdf`. Rebuild it with `build_report.py`; the script uses the verified values below and the published-dashboard screenshot in `report/assets/`.

Verified Databricks KPIs from the seed-52461 run:

- Net revenue: $172,835.74 (dashboard card: $172.84K)
- Completed orders: 3,636 (dashboard card: 3.64K)
- Average order value: $47.53
- On-time delivery: 27.14% (dashboard card: 27.1%)
- Repeat-customer rate: 83.32% (dashboard card: 83.3%)

Verified leading category: Meat & Seafood - 2,710 units, $50,649.02 net revenue, and $15,531.76 gross profit.

Verified leading store: FreshRoute Oakville 1 - 171 completed orders, 154 unique customers, and $9,477.16 net revenue.

Verified comparison values used in the EDA pages:

- Discount 0%: 3,989 line items, 1.53 average quantity, $67,574.14 net revenue
- Discount 20%+: 879 line items, 1.98 average quantity, $14,864.28 net revenue
- Distance 0-5 km: 689 deliveries, 63.86% on time, 1.48 average delay minutes
- Distance 20+ km: 647 deliveries, 3.55% on time, 11.25 average delay minutes

The separate `SYST52461_Project_Explanation_for_Hazim.pdf` is a study guide, not the official five-page submission report.

Before final submission, run all notebooks in Databricks. If a teammate changes the data-generation or cleaning logic, regenerate the report figures and update the numeric findings so the PDF matches the final Gold tables.
