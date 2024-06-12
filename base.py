import requests
import json
# Define headers
headers = {
    'Authorization': 'Bearer patbSDNBJd7yhwnlF.78288fce3b661c0f0a9009dd13428961de8271edfbe71ee7a854af9657a921b0',
    'Content-Type': 'application/json'
}

# Define data
data = {
    "name": "Apartment Hunting1",
    "tables": [
        {
            "description": "A to-do list of places to visit",
            "fields": [
                {
                    "description": "Name of the apartment",
                    "name": "Name",
                    "type": "singleLineText"
                },
                {
                    "name": "Address",
                    "type": "singleLineText"
                },
                {
                    "name": "Visited",
                    "options": {
                        "color": "greenBright",
                        "icon": "check"
                    },
                    "type": "checkbox"
                }
            ],
            "name": "Apartments"
        }
    ],
    "workspaceId": "wsp6LCb1DA6f39cin"
}

# Define URL
url = 'https://api.airtable.com/v0/meta/bases'

# Send POST request
response = requests.post(url, headers=headers, json=data)

# Print response
base=response.json()
print(base)
base_id=base.get("id")
print(base_id)

c=base.get("tables")
print("")
print(c)
for item in c:
    table_id = item.get('id')

print(table_id)



import requests
url = "https://api.airtable.com/v0/{}/{}".format(base_id, table_id)

headers = {
    "Authorization": "Bearer patbSDNBJd7yhwnlF.78288fce3b661c0f0a9009dd13428961de8271edfbe71ee7a854af9657a921b0",
    "Content-Type": "application/json"
}

data = {
    "records": [
        {
            "fields": {
                "Address": "AT agraharam",
                "Name": "Union Square",
                "Visited": True
            }
        },
        {
            "fields": {
                "Address": "1 Ferry Building",
                "Name": "Ferry Building"
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())  # Print the response content




















