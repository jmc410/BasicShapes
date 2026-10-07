import unittest
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestPolymorphism(unittest.TestCase):

    def test_shapes(self):
        shapes = [
            Circle(0, 0, 2),
            Circle(0, 0, 3),
            Rectangle(4, 5),
            Rectangle(2, 8),
            Square(6)
        ]

        expected_areas = [
            12.566370614359172,
            28.274333882308138,
            20,
            16,
            36
        ]

        for shape, expected in zip(shapes, expected_areas):
            self.assertIsInstance(shape, BasicShape)
            self.assertIsNotNone(shape.name)
            self.assertAlmostEqual(shape.area, expected)


if __name__ == "__main__":
    unittest.main()
