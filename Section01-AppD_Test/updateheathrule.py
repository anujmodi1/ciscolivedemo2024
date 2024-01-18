import json
import requests
import urllib3

urllib3.disable_warnings()

url = "https://kickstarter.saas.appdynamics.com/controller/alerting/rest/v1/applications/10095/health-rules/"
health_rule_id = "51524"  # Replace with the actual health rule ID

# Fetch existing health rule
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + '<token>'  # Replace with your actual token
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
