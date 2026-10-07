import unittest
from basic_shape import BasicShape
from circle import Circle


class TestBasicShape(unittest.TestCase):

    def test_cannot_create_basic_shape(self):
        with self.assertRaises(TypeError):
            BasicShape("Shape")

    def test_name(self):
        circle = Circle(0, 0, 5)
        self.assertEqual(circle.name, "Circle")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 5, "")

    def test_area_read_only(self):
        circle = Circle(0, 0, 5)
        with self.assertRaises(AttributeError):
            circle.area = 10


if __name__ == "__main__":
    unittest.main()



# self reminder: python -m unittest discover -s tests -v