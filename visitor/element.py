"""Element"""

from ielement import IElement
from ivisitor import IVisitor


class ElementA(IElement):
    """Element"""
    def __init__(self):
        self.A = 1

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class ElementB(IElement):
    """Element"""
    def __init__(self):
        self.B = 1

    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class ElementC(IElement):
    """Element"""
    def __init__(self):
        self.C = 1

    def accept(self, visitor: IVisitor):
        visitor.visit(self)
