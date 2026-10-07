import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(10, 5)

    def test_construction(self):
        self.assertEqual(self.rectangle.length, 10)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.area, 50)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 5)

    def test_invalid_length(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "5")

    def test_length_recalculates(self):
        self.rectangle.length = 20
        self.assertEqual(self.rectangle.area, 100)

    def test_width_recalculates(self):
        self.rectangle.width = 10
        self.assertEqual(self.rectangle.area, 100)

    def test_failed_assignment_keeps_old_value(self):
        with self.assertRaises(ValueError):
            self.rectangle.length = -10

        self.assertEqual(self.rectangle.length, 10)
        self.assertEqual(self.rectangle.area, 50)


if __name__ == "__main__":
    unittest.main()

