"""
Blue color
"""

from icolor import Color


class Blue(Color):
    """ Blue color"""

    def __init__(self):
        self.color = "Blue Color"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return self.color
