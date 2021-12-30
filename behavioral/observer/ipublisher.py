"""Publisher interface"""

from abc import ABCMeta, abstractmethod
from isubscriber import ISubscriber


class IPublisher(metaclass=ABCMeta):
    """Publisher interface"""

    @abstractmethod
    def subscribe(self, subscriber: ISubscriber):
        """Add subscriber"""


    @abstractmethod
    def unsubscribe(self, subscriber: ISubscriber):
        """Remove subscriber"""

    @staticmethod
    @abstractmethod
    def notify_subscribers():
        """Notify subscribers"""
