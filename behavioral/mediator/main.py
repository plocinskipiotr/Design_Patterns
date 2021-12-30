"""
Main loop for mediator example
"""

from mediator import Mediator
from car import Car
from bus import Bus

if __name__ == '__main__':
    MEDIATOR = Mediator()

    CAR = Car(MEDIATOR, 'volvo')
    CAR2 = Car(MEDIATOR, 'fiat')
    BUS = Bus(MEDIATOR, 'ikarius')
    BUS2 = Bus(MEDIATOR, 'autosan')

    MEDIATOR.add(CAR)
    MEDIATOR.add(BUS)
    MEDIATOR.add(CAR2)
    MEDIATOR.add(BUS2)

    CAR.start()
    print(CAR)
    print(CAR2)
    print(BUS)
    print(BUS2)
    CAR2.stop()
    print(CAR)
    print(CAR2)
    print(BUS)
    print(BUS2)
    BUS.stop()
    print(CAR)
    print(CAR2)
    print(BUS)
    print(BUS2)
    BUS2.start()
    print(CAR)
    print(CAR2)
    print(BUS)
    print(BUS2)
