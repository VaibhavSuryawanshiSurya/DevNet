from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {"host":"176.16.1.6", "port":"830","username":"cisco","password":"cisco"}

netconf_filter = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:itef-interfaces">
            <interface>
                <name> GigabitEthernet2</name>
            </interface>
        </interfaces>

    </filter>
"""

