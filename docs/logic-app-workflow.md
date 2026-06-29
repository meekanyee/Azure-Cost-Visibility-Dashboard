# Logic App workflow

## What I built

I built a Logic App called `la-cost-alert-notify` that sends an email notification when an Azure budget threshold is crossed. The goal was to make sure the right people get notified before the bill becomes a problem, not after.

## How it works

The Logic App uses an HTTP request trigger. When a budget alert fires in Azure Cost Management, it hits the Logic App endpoint and kicks off the workflow. The workflow then sends a formatted email through Office 365 with the budget name, monthly limit, and a link to the Azure portal to see the full breakdown.

## Workflow diagram

![Logic App Workflow](/images/logic-app-workflow.png)

## What the email looks like

![Logic App email](/images/logic-app-email.png)

## Why I used Logic Apps instead of a script

Logic Apps gives you a visual workflow that anyone can read and modify without touching code. In a small business environment that matters because the person maintaining this system might not be the person who built it.