"""
Collection interface
"""

from abc import ABCMeta, abstractmethod
from iiterator import IIterator


class ICollection(metaclass=ABCMeta):
    """Collection interface"""

    @abstractmethod
    def create_iterator(self) -> IIterator:
        """Return iterator"""
