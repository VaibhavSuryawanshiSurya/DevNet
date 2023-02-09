import requests
import json

url = "https://dashbord.meraki.com/api/v0/organizations"

headers = {
    'X-Cisco-Meraki-API-Key':"13d80c63163d821ef16500fd05d55d8cff900bef",
    'User-Agent':"PostmanRuntime/7.16.3",
    'Accept':"*/*",
    'Cache-Control':"no-cache",
    'Postman-Token':"67a3f4c9-bcb4-43a5-bcde-c05ec3e976af,b27f7dd9-3ebc-4d17-a0a8-d62ab5cafb99",
    'Accept-Encoding':"gzip, deflate, br",
    'Connection':"keep-alive",
    'Reference':"https://dashbord.meraki.com/api/v0/organizations"
}

response = requests.get(url,headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))

for respons_org in response:
    if respons_org['name'] == 'DevNet Sandbox':
        orgId = respons_org[id]

print(orgId)