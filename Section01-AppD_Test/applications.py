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
#appd_token_str = str(appd_token) if appd_token is not None else None

#if appd_token_str is not None:
 #   print("Obtained AppDynamics Token1:", appd_token_str)


# Use the token in the Python script
url = "https://kickstarter.saas.appdynamics.com/controller/rest/applications?output=JSON"
payload = {}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + appd_token_str
}

response = requests.request("GET", url, headers=headers, data=payload)

print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
