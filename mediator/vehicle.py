"""
Vehicle
"""

from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """Vehicle class"""

    @abstractmethod
    def stop(self):
        """start vehicle"""

    @abstractmethod
    def start(self):
        """stop vehicle"""
