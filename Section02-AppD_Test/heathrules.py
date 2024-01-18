import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

url="https://kickstarter.saas.appdynamics.com/controller/alerting/rest/v1/applications/10095/health-rules?output=JSON"
payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + 'eyJraWQiOiI5ZjUzZTZlNC01ZWMxLTQ5NDctOWI4ZC1mODNlZWM1MjNhNjgiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBcHBEeW5hbWljcyIsImF1ZCI6IkFwcERfQVBJcyIsImp0aSI6IjdGZ1NROFZGQkIycldJZ21sQ2ppTWciLCJzdWIiOiJmc29sYWIiLCJpZFR5cGUiOiJBUElfQ0xJRU5UIiwiaWQiOiJkNGNmNGY4Ny1kZGI1LTQzYzAtYTA1Zi05MzNhZWI2YmE1YzIiLCJhY2N0SWQiOiI5ZjUzZTZlNC01ZWMxLTQ5NDctOWI4ZC1mODNlZWM1MjNhNjgiLCJ0bnRJZCI6IjlmNTNlNmU0LTVlYzEtNDk0Ny05YjhkLWY4M2VlYzUyM2E2OCIsImFjY3ROYW1lIjoia2lja3N0YXJ0ZXIiLCJ0ZW5hbnROYW1lIjoia2lja3N0YXJ0ZXIiLCJmbW1UbnRJZCI6bnVsbCwiYWNjdFBlcm0iOltdLCJyb2xlSWRzIjpbXSwiaWF0IjoxNzA1NTc2OTYzLCJuYmYiOjE3MDU1NzY4NDMsImV4cCI6MTcwNTY2MzM2MywidG9rZW5UeXBlIjoiQUNDRVNTIn0.GRYPLvxK320dnVODw1O7aXX-QJ4jG5OIKykCmgg6KMQ'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json)
