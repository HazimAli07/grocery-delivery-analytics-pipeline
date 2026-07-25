# Order Status and Trend Validation

**Owner:** Sweta

**Reviewer:** Omar Leopoldo

## Scope reviewed

I reviewed timestamp parsing, order-status cleaning, the completed-order filter, and the monthly order and revenue analysis in the Silver and Gold notebooks.

## Validation and observed result

The Silver order logic converts the source timestamp into a valid order timestamp and derives `OrderDate`, `YearMonth`, day name, and weekend status. The Gold analysis filters financial KPIs to completed orders before calculating order counts and revenue, so cancelled or otherwise incomplete transactions do not inflate business performance.

The final Gold output contained **3,636 completed orders**, **$172,835.74 net revenue**, and an **average order value of $47.53**. The monthly table groups by the normalized `YearMonth` field and orders the results chronologically, which makes it appropriate for the dashboard trend chart and month filter.

## Conclusion

The timestamp and status rules create a consistent time series and a defensible completed-order population. Any future status category should be reviewed before it is included in revenue KPIs.
