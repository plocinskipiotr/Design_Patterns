"""
Iterator interface
"""

from abc import ABCMeta, abstractmethod


class IIterator(metaclass=ABCMeta):
    """Interface for iterators"""

    @staticmethod
    @abstractmethod
    def get_next():
        """Get next element"""

    @staticmethod
    @abstractmethod
    def has_more() -> bool:
        """Check if iterator reached collections end"""
