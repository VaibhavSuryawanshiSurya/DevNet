import xml.etree.ElementTree as ET

#Get the XML file data 
stream = open("sample.xml", "r")

#Parse the data into ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of root element 
for e in root:
    #Print the stringigied version of the element 

    print('\n',ET.tostring(e))

    #Print the "Id" attribute of the Element object 
    print('\n',e.get("Id"))