""" Interface military unit """

from abc import ABCMeta, abstractmethod


class IMilitaryUnit(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def become_order():
        """becoming an order"""
