"""Subscriber"""

from isubscriber import ISubscriber


class Subscriber(ISubscriber):
    """Subscriber"""
    def __init__(self, number):
        self.number = number
        self.state: int = 0
        self.msg: int = 0

    def update(self, *args):
        """Updates the number of received msg"""
        self.msg += 1
        print('subscriber number ' + str(self.number) + ' ' +
              'new message received ' + str(*args) + ' ' +
              'total number of msg received ' + str(self.msg))
