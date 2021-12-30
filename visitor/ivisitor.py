"""Visitor class"""

from abc import ABCMeta, abstractmethod


class IVisitor(metaclass=ABCMeta):
    """Visitor interface"""

    @abstractmethod
    def visit(self, ele):
        """Visiting element"""
