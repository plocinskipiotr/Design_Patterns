"""Remote interface"""

from abc import ABCMeta, abstractmethod


class IRemote(metaclass=ABCMeta):
    """Remote interface"""
    @property
    @abstractmethod
    def device(self):
        """Getting device instance"""

    @abstractmethod
    def toggle_power(self):
        """Toggling power"""

    @abstractmethod
    def volume_down(self):
        """Decreasing volume"""

    @abstractmethod
    def volume_up(self):
        """Increasing volume"""

    @abstractmethod
    def channel_down(self):
        """Decreasing channel"""

    @abstractmethod
    def channel_up(self):
        """Increasing channel"""
