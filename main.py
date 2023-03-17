import xml.etree.ElementTree as ET
import Coasters_overlap

# text file
try:
    file1 = open("output.txt", 'w')
except:
    print("Cannot open a file")

# xml file
data = ET.Element('data')  # parent root element onto which other tags would be created
element1 = ET.SubElement(data, "items")  # adding a subtag name items inside root tag

for i in range(15):
    Coaster = Coasters_overlap.Coasters_overlap()
    s = Coaster.to_string()
    r = str(Coaster.get_radius())
    L = str(Coaster.get_length())
    file1.write(f"r={r}, L={L}\n")
    s_elem = ET.SubElement(element1, f'item{i + 1}')  # adding subtag under the 'items'
    r_elem = ET.SubElement(s_elem, f'r{i+1}')
    l_elem = ET.SubElement(s_elem, f'l{i+1}')
    r_elem.text = r
    l_elem.text = L
    # s_elem.text = s  # adding text between the 'item{i+1}

b_xml = ET.tostring(data)  # Converting the xml data to byte object, for allowing flushing data to file stream
# with open("output.xml", "wb") as f:  # Opening a file, with operation mode `wb` (write + binary)
#     f.write(b_xml)

try:
    file2 = open("Output.xml", 'wb') # Opening a file, with operation mode `wb` (write + binary)
    file2.write(b_xml)
except:
    print("Cannot open a file")

