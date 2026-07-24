# Team Contributions and GitHub Workflow

The instructor will inspect commit and pull-request history. Every member must work through their own GitHub account. Do not rewrite author names or submit all work from Hazim's account.

| Member | Branch | Required meaningful change | Reviews |
|---|---|---|---|
| Hazim Ali | feature/customers-integration | Validate customer cleaning, customer Gold logic, README and final integration | Shreyansh |
| Mannan | feature/store-performance | Validate store generation/cleaning and store dashboard query | Maheshwar |
| Maheshwar | feature/product-performance | Validate product rules and product/category Gold analysis | Mannan |
| Sweta | feature/order-trends | Validate order timestamps/status and monthly/weekend analysis | Omar |
| Omar Leopoldo | feature/discount-revenue | Validate order-item cleaning, revenue formulas, and discount analysis | Sweta |
| Shreyansh Pankaj | feature/delivery-performance | Validate delivery cleaning, distance bands, and on-time analysis | Hazim |

## Exact workflow for each member

1. Clone the repository and create the branch listed above from `main`.
2. Run/review the cells in the section you own.
3. Make at least one substantive correction, validation, chart improvement, or explanation based on the Databricks output.
4. Commit using your own GitHub identity, for example `Improve delivery distance validation and chart`.
5. Push the branch and open a pull request describing the output you verified.
6. The assigned reviewer checks the code/output and approves before Hazim merges.

A formatting-only edit or adding a name is not a meaningful contribution. The pull request should change analysis or validation and mention an observed result.
