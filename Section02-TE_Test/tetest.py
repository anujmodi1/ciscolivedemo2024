#!/usr/bin/env python
import json, re, sys, os, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

from requests.structures import CaseInsensitiveDict

urllib3.disable_warnings()

# Function to run the shell script and capture its output
def run_shell_script(script):
    result = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

# Run shell script to get te_token
shell_script = """
export VAULT_ADDR=http://dev-vault.cloudkareai.com:8200
vault login -method=userpass username=ciscolivedemo password=<password> --no-print $password
te_token=$(vault kv get --field=token  secrets/creds/te-token)
echo $te_token
"""

te_token = run_shell_script(shell_script)
#print(te_token)


# Use the token in the Python script
url = "https://api.thousandeyes.com/v6/agents.json"
payload = {}
headers = {'Authorization': 'Bearer ' + te_token}
agent_response = requests.request("GET", url, headers=headers, data=payload)
print(agent_response)

agent_list_json = agent_response.json()

agent_list = agent_list_json['agents']
list_of_dictionaries = agent_list
sought_value = "Enterprise"
found_values = []
for dictionary in list_of_dictionaries:
    if dictionary["agentType"] == "Enterprise":
        found_values.append(dictionary)

empty_list = []
for item in found_values:
    agentId = item['agentId']
    print(agentId)
    empty_list.append({'agentId': agentId})

test_name = 'webtest<yourname>'
url = 'https://api.thousandeyes.com/v6/tests/http-server/new.json'
payload = {'interval': '300', 'agents': empty_list, 'testName': test_name,  'url': 'http://app.cloudkareai.com:8080/Supercar-Trader/home.do', 'alertsEnabled': '0'}
header = {'content-type': 'application/json', 'authorization': 'Bearer ' + te_token}
r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(r)
