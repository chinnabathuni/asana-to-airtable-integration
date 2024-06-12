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
            "name": "Task ID",
            "type": "singleLineText"
          },
		  
		  {
            "name": "Assigned",
            "type": "singleLineText"
          },
		  
		  {
            "name": "Due Date",
            "type": "singleLineText"
          },
		  
		  {
            "name": "Description",
            "type": "singleLineText"
          },
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
                "Name": "Task1",
				"Task ID":"123456",
				"Assigned":"chinnabathuni lokesh",
				"Description":"A and AT Test Automation",
				"Due Date":"17/06/2024"
            }
        },
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())  # Print the response content
