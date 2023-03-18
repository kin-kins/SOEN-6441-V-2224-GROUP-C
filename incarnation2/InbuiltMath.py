import math
import xml.etree.ElementTree as ET

class InbuiltMath:
    def sin(self, angle):
        """
        Calculates the sine of a given angle in radians using the math.sin() function.

        Args:
        angle (float): The angle to calculate the sine of, in radians.

        Returns:
        float: The sine of the given angle.
        """
        return math.sin(angle)

    def cos(self, angle):
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

    def pi(self):
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

