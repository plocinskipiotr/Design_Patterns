"""
Interface class for ranged units
"""

from abc import ABCMeta, abstractmethod


class IRangeUnit(metaclass=ABCMeta):
    """Interface for ranged units"""

    @staticmethod
    @abstractmethod
    def shoot():
        """Shooting"""
