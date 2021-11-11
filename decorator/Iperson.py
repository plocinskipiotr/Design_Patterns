"""
Fireman interface
"""

from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    """Person interface"""

    @property
    @abstractmethod
    def age(self):
        """Age"""

    @property
    @abstractmethod
    def name(self):
        """Name"""

    @property
    @abstractmethod
    def surname(self):
        """Surname"""

    @abstractmethod
    def __str__(self):
        """String representation"""
