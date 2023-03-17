from Handmade_math import HandmadeMath


class Coasters_overlap:
    pi = 0.0
    alpha = 0.0
    l = 0.0
    r = 0.0

    def __init__(self):
        self.pi = HandmadeMath.estimate_pi(1000000)
        self.raphson_method()

    def raphson_method(self):
        alpha = self.pi / 2  # initial guess
        self.alpha = alpha
        tolerance = 1e-6
        self.r = float(input("Enter the radius of the circles: "))

        def f(a):
            return a - HandmadeMath.sin(a) - self.pi / 2

        def f_derivative(a):
            return 1 - HandmadeMath.cos(a)

        # Calculating alpha using newton Raphson method

        for i in range(1000):
            alpha_new = alpha - f(alpha) / f_derivative(alpha)
            if abs(alpha_new - alpha) < tolerance:
                break
            alpha = alpha_new
            self.alpha = alpha
        self.l = 2 * self.r * (1 - HandmadeMath.cos(self.alpha / 2))  # length of segment X1X2

    def print_l(self):
        print(self.l)

