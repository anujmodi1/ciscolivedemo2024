import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
url = "https://api.thousandeyes.com/v6/agents.json"
payload={}
headers = {'Authorization': 'Bearer ' + "<token>"}
agent_response = requests.request("GET", url, headers=headers, data=payload)
print(agent_response)

agent_list_json = agent_response.json()
#print(agent_list_json)

agent_list = agent_list_json['agents']
list_of_dictionaries = agent_list
sought_value = "Enterprise"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["agentType"] == "Enterprise"):
        found_values.append(dictionary)
#print(found_values)

empty_list=[]
for item in found_values:
    agentId=item['agentId']
    print(agentId)
    empty_list.append({'agentId': agentId})
print(empty_list)

test_name = '<yourname>test<no>'
url='https://api.thousandeyes.com/v6/tests/agent-to-server/new.json'
payload = {'interval': '300', 'agents': empty_list, 'testName': test_name, 'port': '80', 'server': 'www.thousandeyes.com','alertsEnabled': '0'}
header = {'content-type': 'application/json', 'authorization': 'Bearer ' + 'token'}
r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(r)