"""Subscriber interface"""

from abc import ABCMeta, abstractmethod


class ISubscriber(metaclass=ABCMeta):
    """Subscriber interface"""
    @abstractmethod
    def update(self, *args):
        """Update state"""
