import requests
import base64

""" Generate Base64 encoding using the base64
library """
encoded = base64.b64encode('devnetsandbox-user107@devnetsandbox.onmicrosoft.com:tLPfvp*9'.encode('UTF-8')).decode('ASCII')
print(encoded)



""" Get Customer details given a customerID """
url = "https://management.api.umbrella.com/v1/serviceproviders/serviceProviderId/customers/customerId"

headers = {
    'accept': "application/json",
    'authorization': f"Basic {encoded}"
    }
print(headers)

response = requests.request("GET", url, headers=headers)
print(response.text)
