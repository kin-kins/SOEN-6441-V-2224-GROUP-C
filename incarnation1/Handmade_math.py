class HandmadeMath:

    @staticmethod
    def gregory_leibinz(iterations):
        """
           Calculates an estimate of the value of pi using gregory_leibinz method.

           Parameters:
               iterations (int): The number of iterations to do.

           Raises:
               Exception: if iterations is not a positive integer

           Returns:
               pi_estimate (float): The estimated value of pi.
        """
        if (not (type(iterations) == int)) or iterations < 1:
            raise Exception("input of gregory_leibinz needs to be a positive integer")
        pi = 0
        for x in range(0, iterations):
            numerator = ((-1)**x) * (1**(2 * x + 1))
            denominator = 2 * x + 1
            pi += numerator / denominator
        pi = pi * 4
        return pi

    pi = gregory_leibinz(1000000)

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
