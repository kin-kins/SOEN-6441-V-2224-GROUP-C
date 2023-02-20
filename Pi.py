import random

def estimate_pi(n):
    # Initialize a counter to keep track of the number of points that fall inside the unit circle
    num_points_inside_circle = 0
    # Total number of points generated
    num_points_total = n
    # Loop through n times to generate n random points and check if each point falls inside the unit circle
    for i in range(n):
        # Generate a random x-coordinate and y-coordinate between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # Calculate the squared distance from the origin to the point
        distance_squared = x**2 + y**2
        # Check if the point falls inside the unit circle (distance from origin <= 1)
        if distance_squared <= 1:
            # If the point is inside the unit circle, increment the counter
            num_points_inside_circle += 1
    # Calculate the estimated value of pi using the ratio of the number of points inside the circle to the total number of points
    pi_estimate = 4 * num_points_inside_circle / num_points_total
    # Return the estimated value of pi
    return pi_estimate

# Call the function to estimate pi using 1,000,000 random points and print the result
print(estimate_pi(1000000))
