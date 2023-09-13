import unittest
from geometry.shapes import Circle, Triangle


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, delta=0.01)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, delta=0.01)

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_not_right_triangle(self):
        triangle = Triangle(4, 4, 4)
        self.assertFalse(triangle.is_right_triangle())

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(0, 4, 5)

    def test_ivalid_triangle(self):
        with self.assertRaises(ArithmeticError):
            triangle = Triangle(100, 1, 1)


if __name__ == "__main__":
    unittest.main()
