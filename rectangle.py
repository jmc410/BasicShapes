from basic_shape import BasicShape


class Rectangle(BasicShape):

    def __init__(self, length, width, name="Rectangle"):
        super().__init__(name)
        self._length = None
        self._width = None
        self.length = length
        self.width = width

    @property
    def length(self):
        """Returns the rectangle length."""
        return self._length

    @length.setter
    def length(self, value):
        """Sets the length and recalculate the area."""
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be a number.")
        if value <= 0:
            raise ValueError("Length must be positive.")

        self._length = value

        if self._width is not None:
            self.calc_area()

    @property
    def width(self):
        """Return the rectangle width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width and recalculate the area."""
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number.")
        if value <= 0:
            raise ValueError("Width must be positive.")

        self._width = value

        if self._length is not None:
            self.calc_area()

    def calc_area(self):
        """Calculate and store the rectangles area."""
        self._area = self.length * self.width

