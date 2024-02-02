#!/usr/bin/env python
import json, re, sys, os, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

# Function to run the shell script and capture its output
def run_shell_script(script):
    result = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

# Run shell script to get appd_token
shell_script = """
export VAULT_ADDR=http://dev-vault.cloudkareai.com:8200
vault login -method=userpass username=ciscolivedemo password=<password> --no-print $password
appd_token=$(vault kv get --field=token secrets/creds/appd-token)
echo $appd_token
"""
appd_token = run_shell_script(shell_script)
appd_token_str = str(appd_token)

url = "https://kickstarter.saas.appdynamics.com/controller/alerting/rest/v1/applications/10095/health-rules/"
health_rule_template = {
    "name": "Health Rule yourname1",
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
    'Authorization': 'Bearer ' + appd_token_str
}

response = requests.post(url, headers=headers, json=health_rule_template, verify=False)

print("Health rule created successfully.")

