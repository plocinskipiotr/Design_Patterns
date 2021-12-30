""" single soldier """

from imilitary_unit import IMilitaryUnit


class Soldier(IMilitaryUnit):
    """ single soldier """

    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def __str__(self):
        return self.grade + ' ' + self.name + ' ' + self.surname

    def become_order(self):
        print(self.__str__() + ' become an order!')
