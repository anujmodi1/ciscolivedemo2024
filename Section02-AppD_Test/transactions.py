import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

url="https://kickstarter.saas.appdynamics.com/controller/rest/applications/Supercar-Trader/business-transactions"
payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + '<token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json)
