# Azure Cost Visibility Dashboard

A cost tracking and alerting system built on Azure native services.
This project gives small business owners real time visibility into
their Azure spend before the bill becomes a problem.

## What this project does

It tracks Azure spending, sends automatic email alerts when costs
hit defined thresholds, and displays a dashboard that breaks down
spend in plain English instead of Azure resource names.

## Services used

- Azure Cost Management
- Azure Monitor
- Azure Logic Apps
- Azure Workbooks
- Azure Functions
- Office 365

## Documentation

- [Architecture overview](docs/01-architecture-overview.md)
- [Tagging strategy](docs/02-tagging-strategy.md)
- [Cost Management setup](docs/03-cost-management-setup.md)
- Logic App workflow (in progress)
- Workbooks dashboard (in progress)
- Weekly report function (in progress)

## Infrastructure

Resources are deployed using Terraform. Two environments are
provisioned: dev and prod, each with their own resource group
and storage account tagged for cost tracking.

## Status

Active build. Documentation added as each phase is completed.
