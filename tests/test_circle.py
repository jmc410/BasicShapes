import unittest
import math
from circle import Circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(0, 0, 4)

    def test_construction(self):
        self.assertEqual(self.circle.x_center, 0)
        self.assertEqual(self.circle.y_center, 0)
        self.assertEqual(self.circle.radius, 4)

    def test_area(self):
        self.assertAlmostEqual(self.circle.area, math.pi * 16)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -2)

    def test_invalid_radius(self):
        with self.assertRaises(TypeError):
            Circle(0, 0, "4")

    def test_radius_recalculates(self):
        self.circle.radius = 5
        self.assertAlmostEqual(self.circle.area, math.pi * 25)

    def test_coordinates_do_not_change_area(self):
        old_area = self.circle.area
        self.circle.x_center = 10
        self.circle.y_center = -10
        self.assertEqual(self.circle.area, old_area)

    def test_custom_name(self):
        circle = Circle(0, 0, 2, ("Circle Of Death"))
        self.assertEqual(circle.name, ("Circle Of Death"))


if __name__ == "__main__":
    unittest.main()
