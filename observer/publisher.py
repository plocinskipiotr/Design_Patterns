"""Publisher"""

from isubscriber import ISubscriber
from ipublisher import IPublisher


class Publisher(IPublisher):
    """Publisher"""
    def __init__(self):
        self.subscribers: list[ISubscriber] = list()

    def subscribe(self, subscriber: ISubscriber):
        """Add subscriber"""
        self.subscribers.append(subscriber)
        print('subscriber added')

    def unsubscribe(self, subscriber: ISubscriber):
        """Remove subscriber"""
        self.subscribers.remove(subscriber)
        print('subscriber removed')

    def notify_subscribers(self, *args):
        """Notify subscribers"""
        for item in self.subscribers:
            item.update(*args)

    def send_msg(self, *args):
        """Send msg to subscribers"""
        print('msg sent ' + str(*args))
        self.notify_subscribers(*args)
