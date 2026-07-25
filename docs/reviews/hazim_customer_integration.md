# Customer Cleaning and Final Integration Validation

**Owner:** Hazim Ali
**Reviewer:** Shreyansh Pankaj

## Scope reviewed

- Customer identifiers, city values, email values, ages, and loyalty tiers in the Silver customer transformation.
- Customer joins from Silver into the Gold order and customer-behavior tables.
- End-to-end Bronze, Silver, and Gold execution order and the native Databricks dashboard refresh.

## Validation performed

The customer transformation lowercases and trims email values, standardizes city and loyalty labels, parses registration dates, replaces invalid ages with the valid median, and deduplicates on `CustomerID`. The new customer-integration validation notebook independently confirms unique Silver customer IDs, reconciles each customer's Gold order count, and recomputes the repeat-customer KPI from `customer_behavior_gold`.

All three main pipeline notebooks completed successfully in Databricks. The Gold assertions confirmed unique order rows and non-negative net revenue. The final integrated output contained **3,636 completed orders**, **$172,835.74 net revenue**, an **average order value of $47.53**, and an **83.32% repeat-customer rate**. The published dashboard displays the same rounded KPI values, confirming that the report, dashboard, and Gold tables are synchronized.

The separate customer-integration notebook is supplementary validation code. Its structure and Python syntax were checked, but this document does not claim that it was executed in Databricks. Under the team's original Markdown-review workflow, approval is based on checking this explanation against the already verified Silver and Gold logic and published KPI results.

## Reviewer verification checklist

Before approving, Shreyansh should confirm that:

- the owner is Hazim Ali and the review is submitted from Shreyansh's own GitHub account;
- the documented customer cleaning rules match the Silver notebook;
- the customer joins and repeat-customer calculation match the Gold notebook;
- the four stated business results match the verified dashboard and report; and
- the text distinguishes previously verified Databricks results from supplementary code that was not live-run.

## Conclusion

The customer cleaning and join logic are consistent with the project data dictionary, and the final integration is ready for team review. Any future change to customer deduplication or the completed-order filter should be followed by a full Gold-table refresh and comparison of the five executive KPIs.
