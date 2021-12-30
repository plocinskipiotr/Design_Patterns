"""
Interface class for prototype
"""

from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    """Prototype interface"""

    @abstractmethod
    def clone(self):
        """Interface cloning method"""
