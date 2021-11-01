"""Unit factory interface"""
from abc import ABCMeta, abstractmethod


class IUnitFactory(metaclass=ABCMeta):
    """Factory interface"""

    @staticmethod
    @abstractmethod
    def create_unit(unit: str):
        """Unit factory method"""
