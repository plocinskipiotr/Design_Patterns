"""
Interface service
"""

from abc import ABCMeta, abstractmethod


class IService(metaclass=ABCMeta):
    """Interface Service"""

    @abstractmethod
    def get_data(self):
        """get data"""
