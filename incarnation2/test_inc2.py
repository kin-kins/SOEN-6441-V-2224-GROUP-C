import unittest
import Coasters_overlap


class Test_Handmade_math(unittest.TestCase):

    def test_raphson(self):
        result = Coasters_overlap.Coasters_overlap.raphson_method()
        self.assertAlmostEqual(result, 2.30988, places=3)


if __name__ == "__main__":
    unittest.main()