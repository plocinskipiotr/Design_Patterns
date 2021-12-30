"""Land units classes"""
from iunit import IUnit


class LandUnit(IUnit):
    """Land unit base class"""
    @staticmethod
    def move():
        print("land unit movement")

    @staticmethod
    def attack():
        print("land unit attack")


class Marine(LandUnit):
    """Marine unit class"""
    def __init__(self):
        """Marine constructor"""
        self.name = "MARINE"
        self.hp = 30
        self.dmg = 5
        self.range = 7


class Firebat(LandUnit):
    """Firebat unit class"""

    def __init__(self):
        """Firebat constructor"""
        self.name = "FIREBAT"
        self.hp = 40
        self.dmg = 8
        self.range = 3
