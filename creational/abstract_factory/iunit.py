"""Interface for every unit"""

from abc import ABCMeta, abstractmethod


class IUnit(metaclass=ABCMeta):
    """Unit interface"""

    @staticmethod
    @abstractmethod
    def move():
        """Unit move method"""

    @staticmethod
    @abstractmethod
    def attack():
        """Unit attack method"""
