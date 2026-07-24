-- SYST52461 Grocery Delivery Analytics - Databricks Dashboard Queries
-- Run 03_gold_eda.ipynb first. Save each result as a named dashboard dataset.

-- 1. KPI cards
SELECT TotalNetRevenue, CompletedOrders, AverageOrderValue,
       OnTimeDeliveryRatePct, RepeatCustomerRatePct
FROM workspace.analytics.kpi_gold;

-- 2. Monthly revenue trend
SELECT YearMonth, NetRevenue, CompletedOrders, AverageOrderValue
FROM workspace.analytics.monthly_revenue_gold
ORDER BY YearMonth;

-- 3. Revenue and profit by category
SELECT Category, UnitsSold, NetRevenue, GrossProfit
FROM workspace.analytics.category_performance_gold
ORDER BY NetRevenue DESC;

-- 4. Top ten stores
SELECT StoreName, CompletedOrders, UniqueCustomers, NetRevenue,
       AverageOrderValue, OnTimeRatePct
FROM workspace.analytics.store_performance_gold
ORDER BY NetRevenue DESC
LIMIT 10;

-- 5. Top ten products
SELECT ProductName, Category, UnitsSold, NetRevenue, GrossProfit
FROM workspace.analytics.product_performance_gold
ORDER BY NetRevenue DESC
LIMIT 10;

-- 6. Discount effect
SELECT DiscountBand, AverageQuantity, NetRevenue, LineItems
FROM workspace.analytics.discount_impact_gold
ORDER BY SortOrder;

-- 7. Delivery performance by distance
SELECT DistanceBand, Deliveries, OnTimeRatePct, AverageDelayMinutes
FROM workspace.analytics.delivery_distance_gold
ORDER BY SortOrder;

-- 8. Customer behaviour by loyalty tier
SELECT LoyaltyStatus, Customers, AverageOrders, AverageOrderValue, RepeatRatePct
FROM workspace.analytics.loyalty_behavior_gold
ORDER BY CASE LoyaltyStatus
    WHEN 'Basic' THEN 1 WHEN 'Silver' THEN 2 WHEN 'Gold' THEN 3 WHEN 'Platinum' THEN 4 ELSE 5 END;

-- 9. Weekend versus weekday performance
SELECT CASE WHEN IsWeekend THEN 'Weekend' ELSE 'Weekday' END AS DayType,
       COUNT(DISTINCT OrderID) AS CompletedOrders,
       ROUND(SUM(NetRevenue), 2) AS NetRevenue,
       ROUND(AVG(NetRevenue), 2) AS AverageOrderValue
FROM workspace.analytics.orders_gold
GROUP BY IsWeekend;

-- 10. Payment method share
SELECT PaymentMethod, COUNT(DISTINCT OrderID) AS CompletedOrders,
       ROUND(SUM(NetRevenue), 2) AS NetRevenue
FROM workspace.analytics.orders_gold
GROUP BY PaymentMethod
ORDER BY NetRevenue DESC;
