"""
Main loop for decorator example
"""

from person import Person
from fireman import Fireman
from master_fireman import MasterFireman

if __name__ == '__main__':
    PersonInstance = Person('person', 'person', 18)
    FiremanInstance = Fireman(Person('fireman', 'fireman', 25))
    MasterFiremanInstance = MasterFireman(FiremanInstance)
    MasterFiremanInstance2 = MasterFireman(PersonInstance)

    print(PersonInstance)
    print(FiremanInstance)
    print(MasterFiremanInstance)
    print(MasterFiremanInstance2)
