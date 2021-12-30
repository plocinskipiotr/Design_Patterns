"""Strategy interface"""

from abc import ABCMeta, abstractmethod


class IStrategy(metaclass=ABCMeta):
    """Strategy interface"""

    @abstractmethod
    def execute(self, data):
        """strategy method"""
