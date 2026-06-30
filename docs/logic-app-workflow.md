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

## Known limitation

I built an action group (`ag-cost-dashboard-alert`) intended to connect the budget's alert conditions directly to this Logic App, so the email would fire automatically the moment a threshold is crossed, no manual trigger needed.

The Azure portal's budget alert UI only supports email recipients directly. It does not expose an option to attach an action group from that screen, even though action groups exist as a resource type built for this exact purpose. Wiring the two together would require calling the Consumption Budget API directly through Azure CLI or Terraform rather than the portal UI.

For this project the Logic App is verified working independently (see the email screenshot above), and the action group is deployed and ready to be wired in once I have the API call configured. I'm documenting this as a known gap rather than working around it, since understanding where a tool's UI falls short is part of the job.