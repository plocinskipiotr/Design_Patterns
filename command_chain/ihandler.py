""" Interface handler """

from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    """ Interface handler """

    @abstractmethod
    def set_next(self, handler):
        """ Setting next handler """

    @abstractmethod
    def handle(self, request):
        """ Handling request """
