"""
Interface communication device
"""

from abc import ABCMeta, abstractmethod


class IDevice(metaclass=ABCMeta):
    """Interface communication device"""

    @abstractmethod
    def is_enabled(self):
        """Checking stand"""

    @abstractmethod
    def enable(self):
        """Enabling device"""

    @abstractmethod
    def disable(self):
        """Disabling device"""

    @abstractmethod
    def get_volume(self):
        """Get device volume"""

    @abstractmethod
    def get_channel(self):
        """Getting channel"""

    @abstractmethod
    def set_channel(self, value):
        """Setting channel"""
