import requests
import json

################ Login ##############
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url=url, auth=(user,pw), verify=False).json()
# print(response)
token = response['Token']


############## Get Client Details #########

macAdress = '50:61:bf:ec:07:80'
url = f"https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-detail?timestamp=&macAddress={macAdress}"

header = {
    'x-auth-token' : token,
    'User-Agent': "PostmanRuntime/7.30.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "sandboxdnac2.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"

}

response = requests.get(url=url, headers=header, verify=False).json()

print(json.dumps(response, indent=2,sort_keys=True))