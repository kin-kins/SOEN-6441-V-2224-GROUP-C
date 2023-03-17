import random


class HandmadeMath:
    @staticmethod
    def estimate_pi(n):
        # Initialize a counter to keep track of the number of points that fall inside the unit circle
        num_points_inside_circle = 0
        # Total number of points generated
        num_points_total = n
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
        pi_estimate = 4 * num_points_inside_circle / num_points_total
        # Return the estimated value of pi
        return pi_estimate

    @staticmethod
    def factorial(x):  # recursive calculation of factorial
        if x < 0:
            raise Exception("Sorry, no numbers below zero for factorials")
        if x == 0:
            return 1
        if x == 1:
            return 1
        else:
            return HandmadeMath.factorial(x - 1) * x

    @staticmethod
    def cos(x, n=10):  # Calculation of cos(x) using taylor series with n(default = 10) elements
        result = 0
        for i in range(0, n + 1):
            result += ((-1) ** i) * ((x ** (2 * i)) / (HandmadeMath.factorial(2 * i)))
        return result

    @staticmethod
    def sin(x, n=10):  # sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...   taylor series
        result = 0
        sign = 1
        for i in range(1, 2 * n, 2):
            term = sign * (x ** i) / HandmadeMath.factorial(i)
            result += term
            sign *= -1
        return result


'''
    # Call the function to estimate pi using 1,000,000 random points and print the result
    pi = estimate_pi(1000000)

    alpha = pi / 2  # intial guess
    tolerance = 1e-6
    R = float(input("Enter the radius of the circles: "))


# Calculating alpha using newton raphson method

for i in range(1000):
    alpha_new = alpha - f(alpha) / f_derivative(alpha)
    if abs(alpha_new - alpha) < tolerance:
        break
    alpha = alpha_new

l = 2*R*(1 - cos(alpha/2))  # length of segment X1X2
print(f"The length of segment X1X2 is: {l}")
'''