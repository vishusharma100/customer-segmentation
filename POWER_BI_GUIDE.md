# Power BI Dashboard Guide

## Data
Use `customer_segments_powerbi.csv`.

## Suggested visuals
1. Cards:
   - Total Customers = DISTINCTCOUNT(CustomerID)
   - Average Income = AVERAGE(AnnualIncome_k)
   - Average Spending Score = AVERAGE(SpendingScore)
   - Total Spend = SUM(TotalSpend)

2. Donut: Segment by CustomerID count
3. Scatter: AnnualIncome_k on X, SpendingScore on Y, Segment as legend
4. Bar: Segment by Average TotalSpend
5. Bar: Segment by Average PurchaseFrequency
6. Slicers: Gender, Age, Segment

## Dashboard title
Customer Segmentation Dashboard

## Recommended story
Start with customer size and spending KPIs, then show segment distribution, income-vs-spending behavior, and segment-level purchase behavior.
