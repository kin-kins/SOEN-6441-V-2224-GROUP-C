import random


class PiEstimator:
    def __init__(self, n):
        # Initialize instance variables to keep track of the number of
        # points inside the unit circle and the total number of points
        self.n = n
        self.num_points_inside_circle = 0
        self.num_points_total = n

    def estimate_pi(self):
        # Loop through n times to generate n random points and check if each point falls inside the unit circle
        for i in range(self.n):
            # Generate a random x-coordinate and y-coordinate between 0 and 1
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            # Calculate the squared distance from the origin to the point
            distance_squared = x**2 + y**2
            # Check if the point falls inside the unit circle (distance from origin <= 1)
            if distance_squared <= 1:
                # If the point is inside the unit circle, increment the counter
                self.num_points_inside_circle += 1
        # Calculate the estimated value of pi
        # using the ratio of the number of points inside the circle to the total number of points
        pi_estimate = 4 * self.num_points_inside_circle / self.num_points_total
        # Return the estimated value of pi
        return pi_estimate

def main():
    try:
        # Prompt the user to enter the number of points to use for the estimation (default to 1000000)
        n = input("Enter the number of points to use for the estimation (default 1000000): ")
        if not n:
            n = 1000000
        else:
            n = int(n)
        if n <= 0:
            raise ValueError("Number of points must be greater than zero.")
        # Create a PiEstimator object with the specified number of points
        estimator = PiEstimator(n)
        # Call the estimate_pi method to estimate the value of pi
        pi_estimate = estimator.estimate_pi()
        # Print the estimated value of pi
        print("Estimated value of pi:", pi_estimate)
    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except:
        print("An error occurred while running the program.")


if __name__ == '__main__':
    main()
