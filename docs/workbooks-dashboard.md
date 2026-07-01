# Workbooks dashboard

## What I built

I built a custom Azure Workbook called `Cost Visibility Dashboard` with two panels. The reason I built it is because Cost Management already shows what you're spending but it doesn't show what you actually have running. I wanted both questions answered in one place.

## Resource inventory panel

This panel shows every resource in the subscription with its name, type, resource group, environment tag, project tag, and location. It's basically a live list of everything that exists and how it's labeled.

![Resource inventory](/images/workbook-resource-inventory1.png)

## Resource count panel

This panel is a bar chart that shows how many resources are in each resource group split by environment. The whole point is to give a quick visual answer to whether dev or prod has more stuff running, which matters when you're trying to figure out why one environment costs more than the other.

![Resource count chart](/images/workbook-resource-count-chart.png)

## A problem I ran into

My first query kept failing and I couldn't figure out why. Turns out `project` is a reserved keyword in KQL so when I referenced `tags.project` it broke the query even though it looked correct. The fix was switching to bracket notation `tags["project"]` just for that tag. Small thing but it took a while to find.

## What comes next

The dashboard updates in close to real time when Resource Graph data changes. The next piece is the weekly Azure Function which pulls actual cost numbers and emails a comparison showing what changed week over week instead of just a live snapshot.