# Workbooks dashboard

## What I built

I built a custom Azure Workbook called `Cost Visibility Dashboard` with two panels. One shows a full inventory of tagged resources broken down by environment and project. The other shows a bar chart of resource counts grouped by resource group.

## Why I built it this way

Resource Graph doesn't expose live dollar costs directly, only Cost Management does, and I already built those views earlier. So instead of duplicating that, this dashboard adds context Cost Management doesn't show on its own: which resources exist where, how they're tagged, and how many live in each environment.

Put together, the Cost Management views answer "what are we spending" and this Workbook answers "what do we actually have running." Both questions matter when you're trying to explain a bill to someone who isn't an engineer.

## Resource inventory panel

A table query against Azure Resource Graph that lists every resource with its name, type, resource group, environment tag, project tag, and location.

![Resource inventory](/images/workbook-resource-inventory1.png)

## Resource count panel

A bar chart summarizing how many resources live in each resource group, split by environment. It's a fast visual check on whether dev or prod has grown out of proportion.

![Resource count chart](/images/workbook-resource-count-chart.png)

## A KQL issue I ran into

The first version of my query kept failing with a parser error. Turned out `project` is a reserved keyword in KQL, so referencing `tags.project` directly broke the query even though it looked fine. The fix was using bracket notation, `tags["project"]`, for that one tag while keeping dot notation for the others. Small thing, but it cost me a while to track down.

## What comes next

Right now this dashboard updates whenever Resource Graph data changes, which is close to real time. The next piece is the weekly Azure Function report, which will pull actual cost numbers and email a week over week comparison instead of just showing a live snapshot.