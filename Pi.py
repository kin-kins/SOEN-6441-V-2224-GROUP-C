import random

def estimate_pi(n):
    num_points_inside_circle = 0
    num_points_total = n
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_squared = x**2 + y**2
        if distance_squared <= 1:
            num_points_inside_circle += 1
    pi_estimate = 4 * num_points_inside_circle / num_points_total
    return pi_estimate

print(estimate_pi(1000000))