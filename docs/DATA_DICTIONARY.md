# Data Dictionary

## Bronze and Silver tables

| Table | Primary key | Important foreign keys | Purpose and main Silver rules |
|---|---|---|---|
| customers | CustomerID | - | Customer profile and loyalty; deduplicate, normalize text/email, parse registration date, median-impute valid age. |
| stores | StoreID | - | Store location/type; normalize labels and median-impute ratings outside 1-5. |
| products | ProductID | StoreID | Store product catalog; clean price/cost/inventory, reject invalid numbers and orphan stores. |
| orders | OrderID | CustomerID, StoreID | Order event; parse timestamps, normalize status/payment, reject invalid keys, derive calendar fields. |
| order_items | OrderItemID | OrderID, ProductID | Purchased product lines; clean quantity/price/discount, reject invalid rows and cross-store mismatches. |
| deliveries | DeliveryID | OrderID | Driver and fulfilment result; clean units, reject invalid distances, derive delay and on-time indicator. |

## Gold tables

| Table | Grain | Dashboard use |
|---|---|---|
| sales_line_gold | One valid completed order item | Revenue/profit, categories, products, and discounts. |
| orders_gold | One completed order | True average order value, monthly/store/payment analysis, and delivery outcome. |
| store_performance_gold | One store | Revenue, orders, customers, AOV, and on-time rate. |
| product_performance_gold | One product | Units, revenue, profit, and discount. |
| customer_behavior_gold | One purchasing customer | Order frequency, spend, AOV, last order, and repeat flag. |
| monthly_revenue_gold | One month | Revenue trend and completed-order volume. |
| category_performance_gold | One category | Units, revenue, and profit. |
| discount_impact_gold | One discount band | Average quantity and revenue. |
| delivery_distance_gold | One distance band | Delivery count, on-time rate, and average delay. |
| loyalty_behavior_gold | One loyalty tier | Customer count, order frequency, AOV, and repeat rate. |
| kpi_gold | One row | Dashboard headline metrics. |

## Metric definitions

- GrossRevenue = Quantity x UnitPrice
- DiscountAmount = GrossRevenue x DiscountPct
- NetRevenue = GrossRevenue - DiscountAmount
- GrossProfit = NetRevenue - (Quantity x UnitCost)
- AverageOrderValue = average of order-level NetRevenue
- OnTimeRate = delivered orders where ActualMinutes <= PromisedMinutes / delivered orders
- RepeatCustomerRate = customers with at least two completed orders / purchasing customers
