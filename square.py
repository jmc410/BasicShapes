from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side, name="Square"):
        super().__init__(side, side, name)
        self._side = side

    @property
    def side(self):
        """Return the square side."""
        return self._side

    @side.setter
    def side(self, value):
        """Sets the side and keeps length and width equal to eachother."""
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be a number.")
        if value <= 0:
            raise ValueError("Side must be positive.")

        self._side = value
        self._length = value
        self._width = value
        self.calc_area()

    @Rectangle.length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be a number.")
        if value <= 0:
            raise ValueError("Length must be positive.")

        self._length = value

        if hasattr(self, "_side"):
            self._side = value
            self._width = value

        if self._width is not None:
            self.calc_area()

    @Rectangle.width.setter
    def width(self, value):
        """Set width while keeping the square invariant."""
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number.")
        if value <= 0:
            raise ValueError("Width must be positive.")

        self._width = value

        if hasattr(self, "_side"):
            self._side = value
            self._length = value

        if self._length is not None:
            self.calc_area()
