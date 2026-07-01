import azure.functions as func
import datetime
import logging
import os
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

app = func.FunctionApp()

@app.timer_trigger(
    schedule="0 0 8 * * 1",  # Every Monday at 8am
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def weekly_cost_report(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("Timer is past due.")

    logging.info("Weekly cost report function started.")

    # Get current and previous week date ranges
    today = datetime.datetime.utcnow()
    this_week_end = today.strftime("%Y-%m-%d")
    this_week_start = (today - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    last_week_start = (today - datetime.timedelta(days=14)).strftime("%Y-%m-%d")
    last_week_end = this_week_start

    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    scope = f"/subscriptions/{subscription_id}"

    try:
        credential = DefaultAzureCredential()
        client = CostManagementClient(credential)

        # Query this week's costs
        this_week_query = {
            "type": "ActualCost",
            "timeframe": "Custom",
            "timePeriod": {
                "from": this_week_start,
                "to": this_week_end
            },
            "dataset": {
                "granularity": "None",
                "aggregation": {
                    "totalCost": {
                        "name": "Cost",
                        "function": "Sum"
                    }
                },
                "grouping": [
                    {
                        "type": "Dimension",
                        "name": "ServiceName"
                    }
                ]
            }
        }

        # Query last week's costs
        last_week_query = {
            "type": "ActualCost",
            "timeframe": "Custom",
            "timePeriod": {
                "from": last_week_start,
                "to": last_week_end
            },
            "dataset": {
                "granularity": "None",
                "aggregation": {
                    "totalCost": {
                        "name": "Cost",
                        "function": "Sum"
                    }
                },
                "grouping": [
                    {
                        "type": "Dimension",
                        "name": "ServiceName"
                    }
                ]
            }
        }

        this_week_result = client.query.usage(scope, this_week_query)
        last_week_result = client.query.usage(scope, last_week_query)

        # Parse results
        this_week_costs = {}
        for row in this_week_result.rows:
            service = row[1] if row[1] else "Unknown"
            cost = round(float(row[0]), 4)
            this_week_costs[service] = cost

        last_week_costs = {}
        for row in last_week_result.rows:
            service = row[1] if row[1] else "Unknown"
            cost = round(float(row[0]), 4)
            last_week_costs[service] = cost

        # Build comparison report
        all_services = set(list(this_week_costs.keys()) + list(last_week_costs.keys()))
        report_lines = [
            f"Weekly Cost Report",
            f"Period: {this_week_start} to {this_week_end}",
            f"",
            f"{'Service':<40} {'This Week':>12} {'Last Week':>12} {'Change':>12}",
            f"{'-'*76}"
        ]

        total_this_week = 0
        total_last_week = 0

        for service in sorted(all_services):
            this = this_week_costs.get(service, 0)
            last = last_week_costs.get(service, 0)
            change = this - last
            total_this_week += this
            total_last_week += last
            report_lines.append(
                f"{service:<40} ${this:>10.4f} ${last:>10.4f} ${change:>+10.4f}"
            )

        report_lines.append(f"{'-'*76}")
        report_lines.append(
            f"{'TOTAL':<40} ${total_this_week:>10.4f} ${total_last_week:>10.4f} ${total_this_week - total_last_week:>+10.4f}"
        )

        report = "\n".join(report_lines)
        logging.info(f"\n{report}")

    except Exception as e:
        logging.error(f"Error generating cost report: {str(e)}")
        raise