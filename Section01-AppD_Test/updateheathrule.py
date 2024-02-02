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
health_rule_id = "51572"  # Replace with the actual health rule ID

# Fetch existing health rule
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + appd_token_str
}

response = requests.get(url + health_rule_id, headers=headers, verify=False)

if response.status_code == 200:
    # Parse existing health rule configuration
    existing_health_rule = response.json()

    # Update the health rule configuration
    existing_health_rule['enabled'] = True  # Set 'enabled' to True to enable the health rule

    # Make a PUT request to update the health rule
    update_response = requests.put(url + health_rule_id, headers=headers, json=existing_health_rule, verify=False)

    if update_response.status_code == 200:
        print("Health rule updated successfully.")
    else:
        print(f"Failed to update health rule. Status code: {update_response.status_code}")
        print(update_response.text)
else:
    print(f"Failed to fetch existing health rule. Status code: {response.status_code}")
    print(response.text)
