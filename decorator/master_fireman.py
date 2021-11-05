"""
Master fireman class should be decorated fireman class
It implements iperson interface
"""

from iperson import IPerson


class MasterFireman(IPerson):
    """Master fireman class, decorated person"""

    def __init__(self, iperson, grade='master'):
        self.person = iperson
        self.grade = grade

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
        return True

    @property
    def grade(self):
        """Firemaster Grade"""
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def __str__(self):
        return 'Name: ' + self.name + '\nSurname: ' + self.surname + \
               '\nAge: ' + str(self.age) + '\nFire_eq: ' + str(self.fire_eq) \
               + '\nGrade: ' + self.grade
