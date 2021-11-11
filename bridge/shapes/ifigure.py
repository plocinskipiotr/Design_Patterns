"""
Figure interface
"""

from abc import ABCMeta, abstractmethod


class IFigure(metaclass=ABCMeta):
    """
    Figure interface
    """

    @property
    @abstractmethod
    def color(self):
        "returns color instance"

    @abstractmethod
    def perimeter(self):
        "returns perimeter"

    @abstractmethod
    def field(self):
        "returns field"
