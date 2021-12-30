"""Element interface"""

from abc import ABCMeta, abstractmethod


class IElement(metaclass=ABCMeta):
    """Element interface"""
    @abstractmethod
    def accept(self, visitor):
        """Accepting visitor"""
