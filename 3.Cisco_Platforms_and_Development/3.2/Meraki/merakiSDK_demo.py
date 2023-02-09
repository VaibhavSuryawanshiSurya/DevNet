from meraki_sdk.meraki_sdk_client import MerakiSdkClient

X_CISCO_MERAKI_API_KEY ='96638d52e292e689aeb67ebc841bd22058e5eb1d' #replace this value with your generated API keys
MERAKI =MerakiSdkClient(X_CISCO_MERAKI_API_KEY)
ORGS = MERAKI.organizations.get_organizations()
for ORG in ORGS:
    print("Org ID: {} and Org Name:{}".format(ORG['id'], ORG['name']))