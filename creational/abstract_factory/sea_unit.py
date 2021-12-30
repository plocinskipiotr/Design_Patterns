"""Sea units classes"""
from iunit import IUnit


class SeaUnit(IUnit):
    """Sea unit base class"""
    @staticmethod
    def move():
        print("sea unit movement")

    @staticmethod
    def attack():
        print("sea unit attack")


class Transporter(SeaUnit):
    """Transporter unit class"""
    def __init__(self):
        self.name = "TRANSPORTER"
        self.hp = 100
        self.dmg = 0
        self.range = 0


class Warship(SeaUnit):
    """Warship unit class"""
    def __init__(self):
        self.name = "WARSHIP"
        self.hp = 200
        self.dmg = 50
        self.range = 15
