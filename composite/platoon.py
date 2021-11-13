""" Soldiers platoon """
from squad import Squad
from imilitary_unit import IMilitaryUnit


class Platoon(IMilitaryUnit):
    """ Soldiers platoon """

    n_platoons = 1

    def become_order(self):
        """ Becoming order """
        print(self.__str__() + ' become an order!')
        for squad in self.squads:
            squad.become_order()

    def __init__(self, squads):
        self.squads: list[Squad] = squads
        self.number = Platoon.n_platoons
        Platoon.n_platoons += 1

    def add(self, squad):
        """ Adding squad to platoon """
        if isinstance(squad, Squad):
            self.squads.append(squad)
        raise Exception('Platoon accepts only squads')

    def remove(self, squad):
        """ Removing squad from platoon """
        if self.squads:
            try:
                self.squads.remove(squad)
            except ValueError:
                print("There is no such a squad: " + squad + " to delete")

    def get_children(self):
        """ Getting squads from platoon """
        return self.squads

    def __str__(self):
        return 'Combat Platoon ' + str(self.number)
