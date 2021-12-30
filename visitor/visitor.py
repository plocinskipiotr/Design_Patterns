"""Visitor"""

from ivisitor import IVisitor
from element import ElementA, ElementB, ElementC
from ielement import IElement


class Visitor(IVisitor):
    """Visitor"""
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0

    def visit(self, ele: IElement):
        if isinstance(ele, ElementA):
            self.A += 1
        if isinstance(ele, ElementB):
            self.B += 1
        if isinstance(ele, ElementC):
            self.C += 1

    def __str__(self):
        return 'A: ' + str(self.A) + '\n' + \
               'B: ' + str(self.B) + '\n' + \
               'C: ' + str(self.C)
