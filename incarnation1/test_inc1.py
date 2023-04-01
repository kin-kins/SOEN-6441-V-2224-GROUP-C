import unittest
import Handmade_math
import Coasters_overlap
import math


class Test_Handmade_math(unittest.TestCase):

    def test_pi(self):
        result1 = Handmade_math.HandmadeMath.gregory_leibinz(100000)
        result2 = math.pi
        self.assertAlmostEqual(result1, result2, places=3)

    def test_factorial1(self):
        result1 = Handmade_math.HandmadeMath.factorial(5)
        result2 = math.factorial(5)
        self.assertAlmostEqual(result1, result2)

    def test_factorial2(self):
        result1 = Handmade_math.HandmadeMath.factorial(25)
        result2 = math.factorial(25)
        self.assertAlmostEqual(result1, result2)

    def test_factorial3(self):
        with self.assertRaises(Exception):
            Handmade_math.HandmadeMath.factorial(-1)

    def test_cos1(self):
        result1 = Handmade_math.HandmadeMath.cos(0)
        result2 = math.cos(0)
        self.assertAlmostEqual(result1, result2, places=3)

    def test_cos2(self):
        result1 = Handmade_math.HandmadeMath.cos(1000)
        result2 = math.cos(1000)
        self.assertAlmostEqual(result1, result2, places=3)

    def test_sin1(self):
        result1 = Handmade_math.HandmadeMath.sin(800)
        result2 = math.sin(800)
        self.assertAlmostEqual(result1, result2, places=3)

    def test_sin2(self):
        result1 = Handmade_math.HandmadeMath.sin(-30)
        result2 = math.sin(-30)
        self.assertAlmostEqual(result1, result2, places=3)

    def test_sin3(self):
        with self.assertRaises(Exception):
            Handmade_math.HandmadeMath.sin("a")

    def test_raphson(self):
        result = Coasters_overlap.Coasters_overlap.raphson_method()
        self.assertAlmostEqual(result, 2.30988, places=5)


if __name__ == "__main__":
    unittest.main()
