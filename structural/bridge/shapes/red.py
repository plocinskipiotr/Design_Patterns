"""
Red color
"""

from icolor import Color


class Red(Color):
    """ Red color"""

    def __init__(self):
        self.color = "Red Color"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return self.color
