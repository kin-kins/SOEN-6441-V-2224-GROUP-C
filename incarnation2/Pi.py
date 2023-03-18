import math
import xml.etree.ElementTree as ET

class PiApproximator:
    def __init__(self):
        pass

    def get_pi_approximation(self):
        """
        Returns an approximation of the value of pi using the math module.

        Returns:
        float: An approximation of the value of pi.
        """
        try:
            return math.pi
        except AttributeError:
            print("Error: math.pi is not defined")
            return None

def main():
    pi_approximator = PiApproximator()
    pi_approx = pi_approximator.get_pi_approximation()

    if pi_approx is not None:
        # Create XML tree
        root = ET.Element("PiApproximation")
        pi_elem = ET.SubElement(root, "Value")
        pi_elem.text = str(pi_approx)

        # Write XML to file
        tree = ET.ElementTree(root)
        tree.write("pi_approximation.xml", xml_declaration=True)

if __name__ == "__main__":
    main()
