"""Fly units classes"""
from iunit import IUnit


class FlyUnit(IUnit):
    """Fly units base class"""
    @staticmethod
    def move():
        print("fly unit movement")

    @staticmethod
    def attack():
        print("fly unit attack")


class Wright(FlyUnit):
    """Wright unit class"""
    def __init__(self):
        self.name = 'WRIGHT'
        self.hp = 70
        self.dmg = 10
        self.range = 10


class Battlecruiser(FlyUnit):
    """Battlecruiser unit class"""
    def __init__(self):
        self.name = 'BATTLECRUISER'
        self.hp = 300
        self.dmg = 30
        self.range = 12
