import xml.etree.ElementTree as ET
from urllib.request import urlopen
from terminaltables import AsciiTable

tree = ET.parse(urlopen("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"))
root = tree.getroot()
table_data=[[]]

for child in root[0]:
    table_data[0].append(child.tag.split("}")[1])

for count in range(len(root)):
    table_data.append([])
    for data in range(len(root[count])):
        table_data[-1].append(root[count][data].text)


table = AsciiTable(table_data)
print (table.table)
