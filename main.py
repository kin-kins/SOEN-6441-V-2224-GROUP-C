import xml.etree.ElementTree as ET
import Coasters_overlap

# text file
try:
    file1 = open("output.txt", 'a')
except:
    print("Cannot open a file")

# xml file
data = ET.Element('data')  # parent root element onto which other tags would be created
element1 = ET.SubElement(data, "items")  # adding a subtag name items inside root tag

for i in range(20):
    Coaster = Coasters_overlap.Coasters_overlap()
    s = Coaster.to_string()
    file1.write(s)
    s_elem = ET.SubElement(element1, f'item{i + 1}')  # adding subtag under the 'items'
    s_elem.text = s  # adding text between the 'item{i+1}

b_xml = ET.tostring(data)  # Converting the xml data to byte object, for allowing flushing data to file stream
with open("output.xml", "wb") as f:  # Opening a file, with operation mode `wb` (write + binary)
    f.write(b_xml)

# Coaster = Coasters_overlap.Coasters_overlap()
#
# print(Coaster.to_string())
