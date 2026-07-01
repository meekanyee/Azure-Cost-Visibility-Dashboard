# Architecture overview

## The problem

A common problem I noticed when businesses move to Azure is they expect lower costs than running their own servers. A few months in the bills start climbing and nobody can explain why. Azure's default billing breakdown doesn't help because it shows line items like "Microsoft.Compute/virtualMachines" and just a dollar amount Business owners and stakeholders can't really interpret that and don't know what to do with it.

## What I built

A cost tracking and alerting pipeline using Azure native services only.

## Services used

**Azure Cost Management** — tracks and categorizes spend across all services in the subscription

**Azure Monitor** — fires alerts when spend crosses $50, $100, and $200

**Azure Logic Apps** — sends email notifications automatically when an alert triggers

**Azure Workbooks** — dashboard showing spend by service, resource group, and week

**Azure Functions** — runs weekly to compare this week's costs against last week's and show where things are trending

**Office 365** — delivers the alert and report emails

## How it all connects

1. Cost Management tracks spend continuously across the subscription
2. A budget is set with percentage based thresholds
3. Monitor alert rules fire when spend hits $50, $100, or $200
4. Each alert kicks off a Logic Apps workflow
5. Logic Apps sends an email to whoever needs to know with the spend details included
6. Workbooks pulls from Cost Management to render a live dashboard
7. A timer triggered Azure Function runs every week and sends a comparison report showing what changed and where costs are trending

## Decisions

I used Logic Apps instead of writing custom code because it makes the workflow readable and editable for whoever takes over the system. It gives you a visual designer that a non technical person can follow and change without breaking anything.

I used Workbooks instead of Power BI because it lives inside the Azure portal, costs nothing extra, and anyone with Reader access can see it. Power BI adds licensing cost and a separate login for a problem that doesn't need it.

## Diagram

<img src="/images/azure_cost_dashboard_architecture.png" width="100%" alt="Architecture diagram"/>