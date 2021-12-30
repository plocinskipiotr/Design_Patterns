"""
Interface class for creators/factories
"""

from abc import ABCMeta, abstractmethod


class ICreator(metaclass=ABCMeta):
    """Interface for creators (factory methods)"""

    @staticmethod
    @abstractmethod
    def create(**kwargs):
        """Factory method"""
