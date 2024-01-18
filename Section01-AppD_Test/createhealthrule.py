import json
import requests
import urllib3

urllib3.disable_warnings()

url = "https://kickstarter.saas.appdynamics.com/controller/alerting/rest/v1/applications/10095/health-rules/"
health_rule_template = {
    "name": "Health Rule <yourname>",
    "enabled": True,
    "useDataFromLastNMinutes": 30,
    "waitTimeAfterViolation": 5,
    "affects": {
        "affectedEntityType": "BUSINESS_TRANSACTION_PERFORMANCE",
        "affectedBusinessTransactions": {
            "businessTransactionScope": "ALL_BUSINESS_TRANSACTIONS"
        }
    },
    "evalCriterias": {
        "criticalCriteria": {
            "conditionAggregationType": "ALL",
            "conditions": [
                {
                    "name": "Condition 1",
                    "shortName": "A",
                    "evaluateToTrueOnNoData": False,
                    "evalDetail": {
                        "evalDetailType": "SINGLE_METRIC",
                        "metricAggregateFunction": "VALUE",
                        "metricPath": "Average CPU Used (ms)",
                        "metricEvalDetail": {
                            "metricEvalDetailType": "BASELINE_TYPE",
                            "baselineCondition": "WITHIN_BASELINE",
                            "baselineName": "All Data - Last 15 Days",
                            "baselineUnit": "PERCENTAGE",
                            "compareValue": 30.5
                        }
                    }
                }
            ]
        }
    }
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + '<token>'  # Replace with your actual token
}

response = requests.post(url, headers=headers, json=health_rule_template, verify=False)

print("Health rule created successfully.")

