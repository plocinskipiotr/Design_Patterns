"""Interface for xml weather class"""

from abc import ABCMeta, abstractmethod


class IXmlWeather(metaclass=ABCMeta):
    """Interface for xml weather class"""

    @abstractmethod
    def get_icon(self):
        """Getting icon from data"""

    @abstractmethod
    def get_humidity(self):
        """Getting humidity from data"""
