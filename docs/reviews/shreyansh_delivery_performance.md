Delivery Distance Performance Validation
Owner: Shreyansh Pankaj

Reviewer: Hazim Ali
Scope reviewed
I reviewed delivery record cleaning, promised and actual delivery-time fields, delay calculation, distance bands, and the on-time delivery analysis in the Silver and Gold notebooks.
Validation and observed result
The delivery transformation retains valid order and distance values, calculates delay as actual minutes minus promised minutes, and marks deliveries on time when the actual duration does not exceed the promise. Gold joins delivery facts to completed orders and filters to records with actual delivery times for the distance analysis.

The final Databricks KPI showed an overall 27.14% on-time delivery rate. The distance analysis uses ordered bands of 0-5 km, 5-10 km, 10-15 km, 15-20 km, and 20+ km, allowing the dashboard to compare delivery reliability as route length increases without alphabetic misordering.
Conclusion
The delivery analysis consistently connects time performance to distance while excluding missing actual durations from the rate calculation. The low overall on-time rate is an operational finding that should be highlighted during the presentation
