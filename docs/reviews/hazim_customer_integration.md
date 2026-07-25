# Customer Cleaning and Final Integration Validation

**Owner:** Hazim Ali
**Reviewer:** Shreyansh Pankaj

## Scope reviewed

- Customer identifiers, city values, email values, ages, and loyalty tiers in the Silver customer transformation.
- Customer joins from Silver into the Gold order and customer-behavior tables.
- End-to-end Bronze, Silver, and Gold execution order and the native Databricks dashboard refresh.

## Validation performed

The customer transformation lowercases and trims email values, standardizes city and loyalty labels, parses registration dates, replaces invalid ages with the valid median, and deduplicates on `CustomerID`. The new customer-integration validation notebook independently confirms unique Silver customer IDs, reconciles each customer's Gold order count, and recomputes the repeat-customer KPI from `customer_behavior_gold`.

All three pipeline notebooks completed successfully in Databricks. The Gold assertions confirmed unique order rows and non-negative net revenue. The final integrated output contained **3,636 completed orders**, **$172,835.74 net revenue**, an **average order value of $47.53**, and an **83.32% repeat-customer rate**. The published dashboard displays the same rounded KPI values, confirming that the report, dashboard, and Gold tables are synchronized. Hazim's validation notebook must be run after Gold and must print `HAZIM_CUSTOMER_VALIDATION_PASSED` before this PR is approved.

## Conclusion

The customer cleaning and join logic are consistent with the project data dictionary, and the final integration is ready for team review. Any future change to customer deduplication or the completed-order filter should be followed by a full Gold-table refresh and comparison of the five executive KPIs.
