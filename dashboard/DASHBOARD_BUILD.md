# Native Databricks Dashboard Build

## Required result

Create one dashboard titled **FreshRoute Grocery Delivery Performance**. Use the Gold tables produced by `03_gold_eda.ipynb`; never connect visuals directly to Bronze.

The published dashboard is available at [FreshRoute Grocery Delivery Performance](https://dbc-c58ab985-c7cd.cloud.databricks.com/dashboardsv3/01f187bb678d15ae91676a0d5422a14e?o=7474657090248704). Its presentation page is titled **Executive Overview** and includes a global Month filter.

## Layout

1. Top row: five KPI cards - total net revenue, completed orders, average order value, on-time delivery rate, and repeat-customer rate.
2. Second row: monthly revenue line chart (two-thirds width) and category revenue bar chart (one-third).
3. Third row: top stores bar chart and top products horizontal bar chart.
4. Fourth row: discount-versus-quantity column chart and on-time rate by distance line chart.
5. Fifth row: loyalty repeat-rate bar chart, weekend/weekday comparison, and payment-method share.

## Visual settings

- Currency: `$#,##0.00`; percentages: `0.0%` or the precomputed `Pct` values.
- Sort months and distance/discount bands using their supplied sort order.
- Use one consistent colour family; reserve orange for delays or negative operational signals.
- Give every chart a conclusion-oriented title, for example `Longer Trips Miss More Delivery Promises`.
- Add a global `YearMonth` filter connected to relevant datasets.

## Ten-minute presentation

- Hazim: scenario, architecture, and KPI cards (1:15).
- Mannan: store performance (1:15).
- Maheshwar: category and product performance (1:15).
- Sweta: monthly and weekend trends (1:15).
- Omar: discount analysis (1:15).
- Shreyansh: delivery and loyalty findings, limitations, conclusion (1:45).
- Reserve approximately one minute for questions.

## Final verification

- Refresh every dataset after the final notebook run.
- Confirm the five cards show `$172.84K`, `3.64K`, `$47.53`, `27.1%`, and `83.3%`, matching the exact values in `kpi_gold` after display rounding.
- Confirm no chart is blank and all sort orders are correct.
- Test the month filter and reset it before presenting.
- Take one full-dashboard screenshot for the report/submission record.
