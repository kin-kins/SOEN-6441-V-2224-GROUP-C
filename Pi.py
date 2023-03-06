import random

class PiEstimator:
    def __init__(self, n):
        self.n = n
        self.num_points_inside_circle = 0
        self.num_points_total = n

    def estimate_pi(self):
        for i in range(self.n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            distance_squared = x**2 + y**2
            if distance_squared <= 1:
                self.num_points_inside_circle += 1
        pi_estimate = 4 * self.num_points_inside_circle / self.num_points_total
        return pi_estimate

# Create a PiEstimator object with n = 1000000
estimator = PiEstimator(1000000)

# Call the estimate_pi method and print the result
print(estimator.estimate_pi())
