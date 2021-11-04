"""Interface for json weather class"""

from abc import ABCMeta, abstractmethod


class IJsonWeather(metaclass=ABCMeta):
    """Interface for json weather class"""

    @abstractmethod
    def get_pressure(self):
        """Getting pressure from data"""

    @abstractmethod
    def get_condition(self):
        """Getting condition from data"""
