"""Drink interface"""

from abc import ABCMeta, abstractmethod


class IDrink(metaclass=ABCMeta):
    """Drink interface"""

    @staticmethod
    @abstractmethod
    def fill():
        """Fill"""

    @staticmethod
    @abstractmethod
    def drink():
        """Drink"""
