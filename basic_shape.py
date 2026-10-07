from abc import ABC, abstractmethod


class BasicShape(ABC):

    def __init__(self, name):
        self.name = name
        self._area = 0

    @property
    def name(self):
        """Return the shape name."""
        return self._name

    @name.setter
    def name(self, value):
        """Sets the name of the shape."""
        if not isinstance(value, str):
            raise TypeError("Name has to be a string.")
        if not value.strip():
            raise ValueError("Name must not be empty.")
        self._name = value

    @property
    def area(self):
        """Return the current area."""
        return self._area

    @abstractmethod
    def calc_area(self):
        """Calculate and store araea of the shape."""
        pass
