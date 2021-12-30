"""
Fireman interface
"""

from abc import ABCMeta, abstractmethod


class IFireman(metaclass=ABCMeta):
    """Fireman interface"""

    @property
    @abstractmethod
    def grade(self):
        """Grade"""

    @staticmethod
    @abstractmethod
    def put_out_the_fire():
        """Ability to put out the fire"""
