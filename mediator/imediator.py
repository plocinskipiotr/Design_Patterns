"""
Mediator interface
"""

from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    """Mediator interface"""

    @abstractmethod
    def notify(self, sender):
        """notify"""
