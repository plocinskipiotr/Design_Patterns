"""
Color
"""

from abc import ABCMeta, abstractmethod


class Color(metaclass=ABCMeta):
    """ Color """
    @property
    @abstractmethod
    def color(self):
        """returns color"""
