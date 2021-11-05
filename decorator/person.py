"""
Person class implements IPerson interface
"""

from iperson import IPerson


class Person(IPerson):
    """Person class"""

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def age(self):
        """Age"""
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def name(self):
        """Name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        """Surname"""
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    def __str__(self):
        return 'Name: ' + self.name + '\nSurname: ' + self.surname + \
               '\nAge: ' + str(self.age)
