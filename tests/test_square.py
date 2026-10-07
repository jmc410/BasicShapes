import unittest
from square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(5)

    def test_construction(self):
        self.assertEqual(self.square.side, 5)
        self.assertEqual(self.square.length, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.area, 25)

    def test_side_changes_everything(self):
        self.square.side = 10

        self.assertEqual(self.square.side, 10)
        self.assertEqual(self.square.length, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.area, 100)

    def test_length_keeps_square(self):
        self.square.length = 8

        self.assertEqual(self.square.side, 8)
        self.assertEqual(self.square.length, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.area, 64)

    def test_width_keeps_square(self):
        self.square.width = 7

        self.assertEqual(self.square.side, 7)
        self.assertEqual(self.square.length, 7)
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.area, 49)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            self.square.side = 0

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            self.square.side = -5

    def test_invalid_side_type(self):
        with self.assertRaises(TypeError):
            self.square.side = "5"

    def test_failed_assignment_keeps_old_values(self):
        with self.assertRaises(ValueError):
            self.square.side = -10

        self.assertEqual(self.square.side, 5)
        self.assertEqual(self.square.length, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.area, 25)


if __name__ == "__main__":
    unittest.main()
