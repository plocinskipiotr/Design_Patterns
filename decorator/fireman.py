"""
Fireman class should be decorated person class
It implements iperson interface
"""

from iperson import IPerson


class Fireman(IPerson):
    """Fireman class, decorated person"""

    def __init__(self, iperson, fire_eq=True):
        self.person = iperson
        self.fire_eq = fire_eq

    @property
    def age(self):
        """Age"""
        return self.person.surname

    @property
    def name(self):
        """Name"""
        return self.person.name

    @property
    def surname(self):
        """Surname"""
        return self.person.surname

    @property
    def fire_eq(self):
        """Fire equipment"""
        return self._fire

    @fire_eq.setter
    def fire_eq(self, value):
        self._fire = value

    def __str__(self):
        return 'Name: ' + self.name + '\nSurname: ' + self.surname + \
               '\nAge: ' + str(self.age) + '\nFire_eq: ' + str(self.fire_eq)
