# Azure Cost Visibility Dashboard

A lot of small and medium sized business owners move to the cloud because someone told them it would be cheaper than running their
own servers. The problem is they have no tools or knowledge to actually check that. The bill shows up every month and they don't know what they're spending, what's driving it, or whether it's trending up or down.

I built this project to fix that. It tracks and monitors Azure spending using Azure native services, sends automatic alerts before the bill becomes a problem, and breaks down costs in plain language a business owner can actually read and act on.

## What this project does

- Tracks spend across all Azure services using Cost Management
- Sends email alerts automatically when spending hits $50, $100,
  and $200 thresholds via Logic Apps
- Displays a live dashboard in Azure Workbooks showing spend by
  service and resource group
- Generates a weekly comparison report using an Azure Function
  that shows what changed from last week and where costs are
  trending

## Architecture diagram

[Architecture diagram](/images/azure_cost_dashboard_architecture.png)

## Services used

| Service | Role |
|---|---|
| Azure Cost Management | Tracks and categorizes spend |
| Azure Monitor | Fires alerts when thresholds are crossed |
| Azure Logic Apps | Sends email notifications automatically |
| Azure Workbooks | Live dashboard showing spend breakdown |
| Azure Functions | Weekly cost comparison report |
| Terraform | All infrastructure deployed as code |

## Infrastructure

Resources are deployed using Terraform across two environments,
dev and prod, each tagged for cost tracking by environment,
project, owner, and cost center. Tagging is enforced at deploy
time so Cost Management can slice spend any way you need without
manual reconciliation.

## Documentation

- [Architecture overview](docs/0architecture-overview.md)
- [Tagging strategy](docs/tagging-strategy.md)
- [Cost Management setup](docs/cost-management-setup.md)
- [Logic App workflow](docs/logic-app-workflow.md)
- [Workbooks dashboard](docs/workbooks-dashboard.md)
- [Weekly report function](docs/weekly-report-function.md)

## How to deploy

1. Clone the repo
2. Update `terraform/terraform.tfvars` with your values
3. Run `terraform init` and `terraform apply` from the terraform folder
4. Configure the budget and Logic App in the Azure portal following the docs
5. Deploy the function using `func azure functionapp publish`