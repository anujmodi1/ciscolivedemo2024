import requests
import json
url = "https://api.thousandeyes.com/v6/agents.json"
payload={}
headers = {'Authorization': 'Bearer ' + "363b554e-6e5c-427c-9406-f08bcc3feb99"}
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