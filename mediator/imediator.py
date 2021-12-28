"""
Mediator interface
"""

from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):

    @abstractmethod
    def notify(self, sender):
        """notify"""
