""" Get Customer details given a customerID """
import requests

url = "https://management.api.umbrella.com/v1/serviceproviders/serviceProviderId/customers/customerId"

headers = {
    'accept': "application/json",
    'authorization': "Basic ZGV2bmV0c2FuZGJveC11c2VyMTA3QGRldm5ldHNhbmRib3gub25taWNyb3NvZnQuY29tOnRMUGZ2cCo5"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)
