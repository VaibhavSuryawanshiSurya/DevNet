from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '13d80c63163d821ef16500fd05d55d8cff900bef'
meraki = MerakiSdkClient(token)

# Get Organization
orgs = meraki.organizations.get_organizations()
pprint(orgs)

for org in orgs:
    if org['name'] == 'Surya Techanologies':
        organization_id = org['id']

print('Organization Id:',organization_id)


# Get Organization Network
params = {} 
params['organization_id'] = organization_id

networks = meraki.networks.get_organization_networks(params) 
pprint(networks)

for network in networks:
    if network['name'] == 'MerakiSDK-1':
        network_id = network['id']

print("Network Id",network_id)

# Create Network

# Update Network

update = {}
update['network_id'] = network_id

# Delete Network
meraki.networks.delete_network(network_id)

print('\n Output after Delete \n')
networks = meraki.networks.get_organization_networks(params) 
pprint(networks)


# Get Netwotk Devices
# devices = meraki.devices.get_network_devices(network_Id)
# print(type(devices))
# print("Network Device:",devices)














# vlans = meraki.vlans.get_network_vlans(network_Id)
# print(type(vlans))
# pprint(vlans)

