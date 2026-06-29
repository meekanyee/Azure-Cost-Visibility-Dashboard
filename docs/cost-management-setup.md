# Cost Management setup

## What I configured

The two things I configured in Azure Cost Management was a budget with alert thresholds and two custom views that break down spend in ways a business owner can read.

## Budget

I created a monthly budget called `budget-cost-dashboard` and set it to $200/month. It has 3 alert thresholds:

- 25% ($50) early warning
- 50% ($100) midpoint check
- 100% ($200) limit reached

When any threshold gets hit, Azure sends an email alert. Nobody gets surprised by a bill because the alerts fire before it arrives.

## Cost views

### Cost by resource group

I set up a view that shows spend split between `rg-cost-dashboard-dev` and `rg-cost-dashboard-prod`. This answers the most common question a small business has, which is which environment is costing more this month.

![Cost by resource group](/images/cost-by-resource-group.png)

### Cost by service name

I set up a second view that breaks down spend by service type like Storage, Bandwidth, and Compute. This is the translation layer the whole project is built around Instead of showing raw Azure resource IDs, it shows line items a non-technical person can read and actually question.

![Cost by service](/images/cost-by-service.png)

## Why this matters

Most small businesses that move to Azure have no idea what is driving their bill until it arrives. These two views give anyone with Reader access to the subscription a real-time answer to what they are spending and where it is going, no Azure knowledge required.

## What comes next

The budget alerts are configured but not connected to anything yet. The next step is building a Logic Apps workflow that sends a formatted email notification when a threshold is crossed.