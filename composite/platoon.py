""" soldiers platoon """
from squad import Squad
from imilitary_unit import IMilitaryUnit


class Platoon(IMilitaryUnit):
    """ soldiers platoon """

    def become_order(self):
        print(self.__str__() + ' become an order!')
        for squad in self.squads:
            squad.become_order()

    def __init__(self, squads, n=1):
        self.squads: list[Squad] = squads
        self.n = n

    def add(self, squad):
        if isinstance(squad, Squad):
            self.squads.append(squad)
        raise Exception('Platoon accepts only squads')

    def remove(self, squad):
        if self.squads:
            try:
                self.squads.remove(squad)
            except(ValueError):
                raise ValueError("There is no such a squad " + squad + " in platoon")

    def getChildren(self):
        return self.squads

    def __str__(self):
        return 'Combat Platoon ' + str(self.n)
