# Discount and Revenue Calculation Validation

**Owner:** Omar Leopoldo

**Reviewer:** Sweta

## Scope reviewed

I reviewed order-item cleaning, quantity and discount validation, the sales-line revenue formulas, and the discount-band analysis in the Gold notebook.

## Validation and observed result

The Silver order-item rules reject invalid identifiers and quantities and constrain discounts before Gold calculations. At the sales-line level, gross revenue is based on quantity multiplied by unit price, net revenue applies the discount percentage, and gross profit subtracts quantity multiplied by unit cost. The Gold validation also checks that net revenue is never negative.

The final completed-order population produced **$172,835.74 net revenue**. The discount analysis groups lines into `0%`, `5%`, `10%`, `15%`, and `20%+` bands and compares average quantity, net revenue, and line count. Keeping the ordered band field prevents the chart from sorting percentage labels alphabetically.

## Conclusion

The revenue formulas are internally consistent and the discount bands support a meaningful comparison of purchasing behavior. Future pricing changes should be tested against the non-negative revenue assertion.
