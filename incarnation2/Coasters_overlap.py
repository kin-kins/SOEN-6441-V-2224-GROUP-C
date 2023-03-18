from InbuiltMath import InbuiltMath


class Coasters_overlap:
    """
    A class that represents two overlapping coasters on a table.
    Class Attributes :
            pi (float): the value of pi generated using Monte Carlo simulation.
            alpha (float): the angle between the two coasters, in radians, calculated
                           using the Newton-Raphson method for alpha - sin(alpha) = pi/2.
    Instance Attributes:
        length (float): the length of the segment that connects the centers of the
            two circles, calculated as 2r(1 - cos(alpha/2)), where r is the radius
            of the coasters.
        r (float): the radius of the coasters, as entered by the user.
    Methods:
        __init__(self): initializes an instance of the Coasters_overlap class.
        raphson_method(self): calculates the value of alpha using the Newton-Raphson
            method with 1000 iterations or until the error tolerance is reached.
        to_string(self): returns a string representation of the Coasters_overlap object.
    """


    def raphson_method(self):
        """
        Calculates the value of alpha using the Newton-Raphson method with 1000 iterations or if the error tolerance is
        reached
        Local variables:
            alpha (float): value of alpha initialized at pi/2.
            tolerance(float) : set at 1e-6
        Returns:
            None.
        Set Object alpha value to the estimation of the root of -> alpha - sin(alpha) = pi/2.
        """
        alpha = self.pi / 2  # initial guess
        alpha = alpha
        tolerance = 1e-6

        def f(a):
            return a - self.sin - self.pi / 2

        def f_derivative(a):
            return 1 - self.cos

        # Calculating alpha using newton Raphson method
        for i in range(1000):
            alpha_new = alpha - f(alpha) / f_derivative(alpha)
            if abs(alpha_new - alpha) < tolerance:
                break
            alpha = alpha_new
        return alpha



    def __init__(self,angle):
        """
        Initializes an instance of the HandmadeMath class.
        The value of pi is generated using Monte Carlo simulation.
        Alpha is the result of the Newton-Raphson method for alpha - sin(alpha) = pi/2.
        radius r is asked to the user
        and the length is calculated from the other elements using the equation l= 2r(1-cos(alpha/2))
        """

        angle = int(angle)
        ob = InbuiltMath()
        self.pi = ob.pi() # class variable
        self.length = 0.0
        self.r = 0.0
        self.sin = ob.sin(angle)
        self.cos = ob.cos(angle)
        while True:
            while True:
                try:
                    r = float(input("Please enter the radius of the circles: "))
                    break
                except ValueError:
                    print("this is not a valid number, try again")
            if r < 0:
                print("Sorry, no numbers below zero for radius")
            else:
                break
        self.r = r
        self.alpha = self.raphson_method()  # class variable
        self.length = 2 * self.r * (1 - ob.cos(self.alpha / 2))

    def to_string(self):
        """
            Returns a string representation of the HandmadeMath object.
            Parameters:
                    Coasters_overlap object (self)
            Returns:
                    s (str): A string representation of the HandmadeMath object,
                            including the length of segment X1X2, alpha, r, and pi.
        """
        s = f"The radius of the circle is {self.r},and  length of segment X1X2 is: {self.length}\n"
        #  with alpha =  {self.alpha}\n r =  {self.r}\n pi =  {self.pi} \n"
        return s

    def get_radius(self):
        return self.r

    def get_length(self):
        return self.length


    def get_pi(self):
        return self.pi
