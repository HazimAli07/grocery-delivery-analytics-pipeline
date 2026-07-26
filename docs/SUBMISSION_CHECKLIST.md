# Final Submission Checklist

## Repository

- [x] Repository is public and accessible to the instructor.
- [x] All six members have genuine commits and at least one merged pull request.
- [x] README contains the final GitHub URL, team accounts, and notebook run order.
- [x] Main branch contains the final merged notebooks and report.

## Databricks

- [x] Run `01_bronze_generation.ipynb` with all assertions passing (8/8 cells live-verified July 26, 2026).
- [x] Run `02_silver_processing.ipynb` with all key checks passing (8/8 cells live-verified July 26, 2026).
- [x] Run `03_gold_eda.ipynb` with all Gold validation passing (10/10 cells and exact KPI output live-verified July 26, 2026).
- [ ] Refresh all dashboard datasets after the last notebook run. A final refresh was requested on July 26, but Databricks Free Edition did not complete it under heavy load; the unchanged published cards still match the freshly verified deterministic Gold results.
- [x] Verify dashboard Month filter, currency, percentages, labels, and sort order. The Month filter was tested and reset to `All` on July 26, 2026.
- [x] Capture one final dashboard screenshot (`report/assets/dashboard_published.jpg`).

### Owner validation status

- [x] `04_hazim_customer_integration_validation.ipynb` printed `HAZIM_CUSTOMER_VALIDATION_PASSED` live.
- [x] `05_mannan_store_performance_validation.ipynb` printed `MANNAN_STORE_VALIDATION_PASSED` live.
- [x] `06_maheshwar_product_category_validation.ipynb` printed `MAHESHWAR_PRODUCT_VALIDATION_PASSED` live.
- [x] `07_sweta_order_trend_validation.ipynb` printed `SWETA_ORDER_TREND_VALIDATION_PASSED` live.
- [x] `08_omar_discount_revenue_validation.ipynb` printed `OMAR_DISCOUNT_REVENUE_VALIDATION_PASSED` live.
- [ ] `09_shreyansh_delivery_performance_validation.ipynb` is imported and statically verified as safe/read-only, but Databricks Free Edition did not schedule its newly imported session during the final live check. The same delivery tables, distance findings, and 27.14% KPI were already validated by the successful Gold notebook and published dashboard.

## Report and presentation

- [x] Report is exactly five readable letter pages and lists all members on page one.
- [x] Final Databricks results match the report and preview figures, so no replacement is needed.
- [x] GitHub URL in the report and prepared SLATE comments is correct.
- [ ] Rehearse the dashboard presentation to stay within ten minutes.
- [ ] One member submits the PDF and repository URL through SLATE before the confirmed deadline.

The two unchecked submission/presentation items require a team member. Nothing has been uploaded or submitted to SLATE.
