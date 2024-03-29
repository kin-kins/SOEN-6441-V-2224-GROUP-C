import xml.etree.ElementTree as ET
import Coasters_overlap

def main():
    try:
        file2 = open("Output.xml", 'wb')  # Opening a file, with operation mode `wb` (write + binary) #../incarnation2/
    except (Exception,):
        raise Exception("Cannot open an xml file")
    # xml file
    data = ET.Element('data')  # parent root element onto which other tags would be created
    element1 = ET.SubElement(data, "list")  # adding a subtag name items inside root tag

    while True:
        while True:
            try:
                coasters_pair_amount = int(input("Please enter the number of coaster pairs you want :"))
                break
            except ValueError:
                print("this is not a valid number, try again")
        if coasters_pair_amount < 1:
            print("please input a positive amount of pairs")
        else:
            break

    for i in range(coasters_pair_amount):
        Coaster = Coasters_overlap.Coasters_overlap()
        s = Coaster.to_string()
        r = str(Coaster.get_radius())
        L = str(Coaster.get_length())
        s_elem = ET.SubElement(element1, f'item')  # adding subtag under the 'items'
        r_elem = ET.SubElement(s_elem, 'r')
        l_elem = ET.SubElement(s_elem, 'l')
        r_elem.text = r
        l_elem.text = L
        s_elem.text = str(i + 1)  # adding text between the 'item{i+1}

    b_xml = ET.tostring(data)  # Converting the xml data to byte object, for allowing flushing data to file stream
    # with open("output.xml", "wb") as f:  # Opening a file, with operation mode `wb` (write + binary)
    #     f.write(b_xml)

    file2.write(b_xml)
    print("Done! Check your output.xml file for the results")


if __name__=="__main__":
    main()
