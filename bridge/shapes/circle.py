"""
Circle
"""

from ifigure import IFigure


class Circle(IFigure):
    """
    Circle
    """

    def __init__(self, ray, color):
        self.ray = ray
        self.color = color

    def perimeter(self):
        return 2 * 3.14 * self.ray

    def field(self):
        return 3.14 * self.ray ** 2

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
