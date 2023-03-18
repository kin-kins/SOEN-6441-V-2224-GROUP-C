import math
import xml.etree.ElementTree as ET

class InbuiltMath:
    def calculate_sine(self, angle):
        """
        Calculates the sine of a given angle in radians using the math.sin() function.

        Args:
        angle (float): The angle to calculate the sine of, in radians.

        Returns:
        float: The sine of the given angle.
        """
        return math.sin(angle)

    def calculate_cosine(self, angle):
        """
        Calculates the cosine of a given angle in radians using the math.cos() function.

        Args:
        angle (float): The angle to calculate the cosine of, in radians.

        Returns:
        float: The cosine of the given angle.
        """
        return math.cos(angle)

    def calculate_factorial(self, n):
        """
        Calculates the factorial of a given positive integer n using the math.factorial() function.

        Args:
        n (int): The integer to calculate the factorial of.

        Returns:
        int: The factorial of n.
        """
        if n < 0:
            raise ValueError("Factorial is undefined for negative integers.")
        else:
            return math.factorial(n)

def main():
    inbuilt_math = InbuiltMath()
    angle_in_radians = math.pi / 4
    try:
        sine = inbuilt_math.calculate_sine(angle_in_radians)
        cosine = inbuilt_math.calculate_cosine(angle_in_radians)
        factorial = inbuilt_math.calculate_factorial(5)
    except ValueError as e:
        print("Error:", e)
    else:
        # Create the root element of the XML file
        root = ET.Element("output")

        # Add the sine, cosine, and factorial elements to the root
        ET.SubElement(root, "sine").text = str(sine)
        ET.SubElement(root, "cosine").text = str(cosine)
        ET.SubElement(root, "factorial").text = str(factorial)

        # Create the XML file
        tree = ET.ElementTree(root)
        tree.write("output.xml")

if __name__ == '__main__':
    main()
