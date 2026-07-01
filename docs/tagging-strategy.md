# Tagging strategy

## Why tagging matters

Without tags Cost Management only shows you spend by service type. You can see that a storage account has costs this month but you can't tell which environment it belongs to, who owns it, or which project it's for. You can't answer "how much did dev cost this month?" Tags fix that. Every resource in this project gets tagged at deploy time so I can slice spend any way I need to.

## Tag schema

**environment** — which environment the resource belongs to
(dev, prod)

**project** — which project owns the resource (cost-dashboard)

**owner** — who is responsible for it

**cost-center** — which team gets charged for it (engineering)

## How enforcement works

Tags are applied through Terraform's default_tags block in the provider configuration. Every resource Terraform deploys inherits the full tag set automatically so nothing gets deployed untagged.

In a real org I would back this up with an Azure Policy set to deny any resource creation that's missing required tags. That way even resources deployed outside of Terraform can't slip through without being labeled.

## What this makes possible

Once every resource is tagged consistently Cost Management can answer questions like:

- How much did the dev environment cost this month vs last month?
- What is the cost-dashboard project spending across all services?
- Which owner's resources are driving the most spend?