import random


class HandmadeMath:
    @staticmethod
    def estimate_pi(n):
        """
        Calculates an estimate of the value of pi using Monte Carlo simulation.

        Parameters:
            n (int): The number of points to be generated for the simulation.

        Raises:
            Exception: if n is not a positive integer

        Returns:
            pi_estimate (float): The estimated value of pi.
        """
        if not (type(n) == int):
            raise Exception("input of estimate_pi needs to be a positive integer")
        # Initialize a counter to keep track of the number of points that fall inside the unit circle
        num_points_inside_circle = 0
        # Loop through n times to generate n random points and check if each point falls inside the unit circle
        for estimate in range(n):
            # Generate a random x-coordinate and y-coordinate between 0 and 1
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            # Calculate the squared distance from the origin to the point
            distance_squared = x ** 2 + y ** 2
            # Check if the point falls inside the unit circle (distance from origin <= 1)
            if distance_squared <= 1:
                # If the point is inside the unit circle, increment the counter
                num_points_inside_circle += 1
        # Calculate the estimated value of pi using the ratio of the number
        # of points inside the circle to the total number of points
        pi_estimate = 4 * num_points_inside_circle / n
        return pi_estimate

    @staticmethod
    def factorial(x):
        """
        Calculates the factorial of x recursively.

        Parameters:
            x (int): The number whose factorial needs to be calculated.

        Raises:
            Exception: if x is not a positive integer or x is less than zero.

        Returns:
            factorial (int): The factorial of x calculated recursively.
        """
        if not (type(x) == int):
            raise Exception("input of factorial needs to be a positive integer")
        if x < 0:
            raise Exception("Sorry, no numbers below zero for factorials")
        if x == 0:
            return 1
        if x == 1:
            return 1
        else:
            return HandmadeMath.factorial(x - 1) * x

    @staticmethod
    def cos(x, n=10):
        """
        Calculates the cosine of x using Taylor series with n (default = 10) elements.
        Parameters:
            x (float): The value in radians for which cosine needs to be calculated
            n (int): The number of terms to be used in Taylor series. Default is 10.
        Returns:
            result (float): The value of cosine of x calculated using Taylor series
        """
        if (not (type(n) == int)) or n <= 0:
            raise Exception("input n of cos needs to be a positive integer")
        result = 0
        for i in range(0, n + 1):
            result += ((-1) ** i) * ((x ** (2 * i)) / (HandmadeMath.factorial(2 * i)))
        return result

    @staticmethod
    def sin(x, n=10):
        """
        Calculates the sine of x using Taylor series with n (default = 10) elements.
        Parameters:
            x (float): The value in radians for which sine needs to be calculated
            n (int): The number of terms to be used in Taylor series. Default is 10.
        Returns:
            result (float): The value of sine of x calculated using Taylor series
        """
        result = 0
        sign = 1
        for i in range(1, 2 * n, 2):
            term = sign * (x ** i) / HandmadeMath.factorial(i)
            result += term
            sign *= -1
        return result
