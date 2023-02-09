from dnacentersdk import api
import json
import time
import calendar


dna = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com',username='devnetuser', 
                        password='Cisco123!', verify=False, version='1.3.0')


################# Authorization ###############

token = dna.authentication.authentication_api(username='devnetuser', password='Cisco123!')
# print(token)

################ get all interface ###########

all_interface = dna.devices.get_all_interfaces(limit=1)
id = all_interface.response[0].id
# print(id)

################ get device list ###########

devices_list = dna.devices.get_device_list()
# print(json.dumps(devices_list, indent=2, sort_keys=True))

############### Site Topology #########

sites = dna.networks.get_site_topology()
# print(sites)
for site in sites.response.sites:
    if site.parentId == '4988a4c1-f2c7-4905-ab92-1f7b3b726519':
        # print(site.name)
        for child_sites in sites.response.sites:
            if child_sites.parentId == site.id:
                # print(f'{child_sites.name}')
                pass
            for more_children in sites.response.sites:
                if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                    # print(f'{more_children.name}')
                    pass
    # print(' ')

        
############### Vlans #########

vlans = dna.networks.get_vlan_details()
# print(vlans)


############### Physical Topology Details #########

phys_top = dna.networks.get_physical_topology()
# print(json.dumps(phys_top, indent=2, sort_keys=True))



############### Client Health Check #########

epoch_datetime = calendar.timegm(time.gmtime())

client_health = dna.clients.get_overall_client_health(timestamp=None)
print(json.dumps(client_health, indent=2, sort_keys=True))


