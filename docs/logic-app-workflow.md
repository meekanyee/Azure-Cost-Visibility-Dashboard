# Logic App workflow

## What I built

I built a Logic App called `la-cost-alert-notify` that sends an email notification when an Azure budget threshold is crossed. The goal was to make sure the right people get notified before the bill becomes a problem.

## How it works

The Logic App uses an HTTP request trigger. When a budget alert fires in Azure Cost Management it hits the Logic App endpoint and kicks off the workflow. The workflow then sends a formatted email through Office 365 with the budget name, monthly limit, and a link to the Azure portal to see the full breakdown.

## Workflow diagram

![Logic App workflow](/images/logic-app-workflow.png)

## What the email looks like

![Logic App email](/images/logic-app-email.png)

## Why I used Logic Apps instead of a script

Logic Apps gives you a visual workflow that anyone can read and modify without touching code. In a small business environment that matters because the person maintaining this system might not be the person who built it.

## Known limitation

I built an action group called `ag-cost-dashboard-alert` that was supposed to connect the budget alert conditions directly to this Logic App so the email fires automatically the moment a threshold is crossed, no manual trigger needed.

The Azure portal's budget alert UI only supports email recipients directly. It does not give you an option to attach an action group from that screen even though action groups exist as a resource type built for exactly this purpose. Wiring the two together would require calling the Consumption Budget API directly through the Azure CLI or Terraform instead of the portal.

The Logic App is verified working on its own as you can see in the email screenshot above. The action group is deployed and ready to be connected once I configure the API call. I documented this as a known gap instead of working around it because knowing where a tool's UI falls short is part of the job.