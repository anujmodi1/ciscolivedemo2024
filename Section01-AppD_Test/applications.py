import requests, json

url="https://kickstarter.saas.appdynamics.com/controller/rest/applications?output=JSON"

payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + '<token>'
}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json)
