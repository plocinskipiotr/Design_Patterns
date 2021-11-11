"""
Master fireman class should be decorated fireman class
It implements iperson interface
"""

from Ifireman import IFireman
from Iperson import IPerson


class MasterFireman(IPerson, IFireman):
    """Master fireman class, decorated person"""

    def __init__(self, name, surname, age, ifireman, grade='master'):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade
        self.fireman = ifireman

    @property
    def age(self):
        """Age"""
        return self._age

    @property
    def name(self):
        """Name"""
        return self._name

    @property
    def surname(self):
        """Surname"""
        return self._surname

    @property
    def grade(self):
        """Grade"""
        return self._grade

    @name.setter
    def name(self, value):
        self._name = value

    @surname.setter
    def surname(self, value):
        self._surname = value

    @age.setter
    def age(self, value):
        self._age = value

    @grade.setter
    def grade(self, value):
        self._grade = value

    @staticmethod
    def put_out_the_fire():
        print(__name__ + " is putting out the fire with super water")

    def __str__(self):
        return 'Name: ' + self.name + '\nSurname: ' + self.surname + \
               '\nAge: ' + str(self.age) + '\nGrade: ' + self.grade
