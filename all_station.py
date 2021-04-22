import xml.etree.ElementTree as ET
from urllib import urlopen
tree = ET.parse(urlopen("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"))
root = tree.getroot()
for x in root[0]:
    print(child.tag.split("}")[1])