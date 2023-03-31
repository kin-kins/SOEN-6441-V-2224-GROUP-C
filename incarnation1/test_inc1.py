import unittest
import Handmade_math
import Coasters_overlap
import math


class Test_Handmade_math(unittest.TestCase):

    def test_pi(self):
        result1 = Handmade_math.HandmadeMath.gregory_leibinz(100000)
        result2 = math.pi
        self.assertAlmostEqual(result1, result2, places=3)

    def test_factorial(self):
        result1 = Handmade_math.HandmadeMath.factorial(5)
        result2 = math.factorial(5)
        self.assertAlmostEqual(result1, result2)

    def test_cos(self):
        result1 = Handmade_math.HandmadeMath.cos(0)
        result2 = math.cos(0)
        self.assertAlmostEqual(result1, result2, places=1)

    def test_sin(self):
        result1 = Handmade_math.HandmadeMath.sin(90)
        result2 = math.sin(90)
        self.assertAlmostEqual(result1, result2, places=1)

    def test_raphson(self):
        result = Coasters_overlap.Coasters_overlap.raphson_method()
        self.assertAlmostEqual(result, 2.30988, places=3)


if __name__ == "__main__":
    unittest.main()
