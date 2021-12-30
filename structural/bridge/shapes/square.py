"""
Square
"""

from ifigure import IFigure


class Square(IFigure):
    """Square"""

    def __init__(self, side, color):
        self.side = side
        self.color = color

    def perimeter(self):
        return 4 * self.side

    def field(self):
        return self.side ** 2

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return __name__ + '\n' + \
               'color: ' + str(self.color) + '\n' + \
               'perimeter: ' + str(self.perimeter()) + '\n' + \
               'field: ' + str(self.field())
