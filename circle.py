import math
from basic_shape import BasicShape


class Circle(BasicShape):
    """Represent a circle with a center point and radius."""

    def __init__(self, x_center, y_center, radius, name="Circle"):
        """Initialize a circle."""
        super().__init__(name)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    @property
    def x_center(self):
        """Return the x-coordinate of the center."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        """Set the x-coordinate. It must be numeric."""
        if not isinstance(value, (int, float)):
            raise TypeError("x_center must be numeric.")
        self._x_center = value

    @property
    def y_center(self):
        """Return the y-coordinate of the center."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        """Set the y-coordinate, has to be a number."""
        if not isinstance(value, (int, float)):
            raise TypeError("y_center must be a number.")
        self._y_center = value

    @property
    def radius(self):
        """Returns the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Sets the radius and recalculate area."""
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number.")
        if value <= 0:
            raise ValueError("Radius must be positive.")

        self._radius = value
        self.calc_area()

    def calc_area(self):
        """Calculate and store area of the circle."""
        self._area = math.pi * self.radius ** 2
