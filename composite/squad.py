""" soldiers squad """
from composite.soldier import Soldier
from imilitary_unit import IMilitaryUnit


class Squad(IMilitaryUnit):
    """ soldiers squad """

    def become_order(self):
        print(self.__str__() + ' become an order!')
        for soldier in self.soldiers:
            soldier.become_order()

    def __init__(self, soldiers, n=1):
        self.soldiers: list[soldiers] = soldiers
        self.n = n

    def add(self, soldier):
        if isinstance(soldier, Soldier):
            self.soldiers.append(soldier)
        raise Exception('Squad accepts only soldiers')

    def remove(self, soldier):
        if self.soldiers:
            try:
                self.soldiers.remove(soldier)
            except(ValueError):
                raise ValueError("There is no such a soldier " + soldier + " in squad")

    def getChildren(self):
        return self.soldiers

    def __str__(self):
        return 'Combat Squad ' + str(self.n)
