# Architecture overview

## The problem

I built this project after learning about a pattern that comes up constantly with business cloud environments. A company usually moves to Azure expecting lower costs than running on their own servers but a few months in the bills start climbing and there isn't an explanation why. Azure's default billing breakdown doesn't help that much because it shows line items like "Microsoft.Compute/virtualMachines" and just a dollar amount. Business owners and stake holders can't really interpret that.

## What I built

A cost tracking and alerting pipeline using Azure native services only.

## Services used

Azure Cost Management
  - Used to track and categorize spend across all the services

Azure Monitor
  - Fires alerts when spend crosses $50, $100, and $200

Azure Logic Apps
  - Sends email notifications when an alert triggers

Azure Workbooks
  - Dashboard showing spend by service, resource group, and week

Azure Functions
  - Runs weekly to compare different week's costs

Office 365
  - Delivers the alert and report emails

## How it all connects

1. Cost management tracks spend continuously across the subscription
2. A budget is set with percentage-based thresholds
3. Monitor alerts rules fire when spend hits $50, $100, or $200
4. Each alert kicks off a Logic Apps workflow
5. Logic Apps sends an email to whoever needs to know, with the spend details included.
6. Workbooks pulls from Cost Management to render a live dashboard
7. A timer-triggered Azure Function runs every week and emails a comparison report showing what changed and where costs are trending


## Decisions

I chose Logic Apps over custom code because it makes the workflow readable and editable for whoever takes over the system. Logic Apps also gives you a visual designer that someone who isn't technical can follow and change without breaking anything.

I chose Workbooks over Power BI because it's in the Azure portal, costs nothings extra, and anyone with Reader access to the subscription can see them. With Power BI you'd have to add licensing cost and a seperate login.


## Diagram

*I'll add a diagram after I complete the build.*
