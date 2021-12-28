"""
Vehicle
"""

from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):

    @abstractmethod
    def stop(self):
        """start vehicle"""
    @abstractmethod
    def start(self):
        """stop vehicle"""