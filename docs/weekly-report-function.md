# Weekly cost report function

## What I built

I built an Azure Function called `weekly_cost_report` that runs every Monday at 8am on a timer trigger. It pulls cost data from Azure Cost Management, compares this week's spend to last week's by service, and logs a formatted comparison report.

## Why I built it

The budget alerts and Cost Management views I set up earlier are good for real time visibility but they don't tell you what changed week over week. A business owner doesn't just want to know what they're spending right now. They want to know if it's going up or down and which service is driving the change. This function answers that automatically every week without anyone having to log into the portal.

## How it works

1. A timer trigger fires every Monday at 8am
2. The function calls the Azure Cost Management API using a managed identity with no stored credentials
3. It queries actual costs for the current week and the previous week grouped by service name
4. It builds a comparison table showing this week, last week, and the dollar change for each service
5. The report gets logged to Azure Function logs

## Deployment

The function is deployed to a Consumption plan so it only runs when triggered and costs nothing while idle. I deployed it using Azure Functions Core Tools from the command line.

![Function deployment](/images/function-deploy-success.png)

The deployment output confirms the function registered as a timer trigger under `func-cost-dashboard-meek`.

## Authentication

Instead of storing credentials the function uses a system assigned managed identity. I gave that identity the Cost Management Reader role scoped to the subscription so it can read spend data without having any other permissions.

## What the report outputs

The function logs a week over week cost comparison table grouped by Azure service name. Each row shows this week's cost, last week's cost, and the dollar change. A total row at the bottom shows the full subscription spend change. The output lives in the Function App's invocation logs in the Azure portal under Logs and Monitor.

## Note on portal testing

Timer triggered functions can't be tested through the Azure portal's Test/Run panel due to CORS restrictions on consumption plan functions. The function runs correctly on its Monday schedule. To test it manually you would trigger it through the Azure CLI using `az functionapp function invoke`.

## What comes next

Right now the report logs to Azure Function logs. The next step would be wiring it to send an email through the same Logic App workflow I built earlier so stakeholders get the weekly comparison in their inbox every Monday without logging in anywhere.