""" soldiers squad """
from soldier import Soldier
from imilitary_unit import IMilitaryUnit


class Squad(IMilitaryUnit):
    """ soldiers squad """

    n_squad = 1

    def become_order(self):
        """Becoming order from squad"""
        print(self.__str__() + ' become an order!')
        for soldier in self.soldiers:
            soldier.become_order()

    def __init__(self, soldiers):
        self.soldiers: list[soldiers] = soldiers
        self.number = Squad.n_squad
        Squad.n_squad += 1

    def add(self, soldier):
        """Adding soldier to squad"""
        if isinstance(soldier, Soldier):
            self.soldiers.append(soldier)
        raise Exception('Squad accepts only soldiers')

    def remove(self, soldier):
        """Removing soldier from squad"""
        if self.soldiers:
            try:
                self.soldiers.remove(soldier)
            except ValueError:
                print("There is no such a soldier " + soldier + " in squad")

    def get_children(self):
        """getting list of squad soldiers"""
        return self.soldiers

    def __str__(self):
        return 'Combat Squad ' + str(self.number)
