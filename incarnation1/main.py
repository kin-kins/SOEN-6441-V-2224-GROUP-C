import xml.etree.ElementTree as ET
import Coasters_overlap

# text file
try:
    file1 = open("../incarnation1/output.txt", 'w') #
except (Exception,):
    raise Exception("Cannot open a txt file")




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
    file1.write(f"r={r}, L={L}\n")





print("Done! Check your output.txt file for the results")
