"""
Main loop for abstract factory example
"""
from abstract_factory import UnitCreator

if __name__ == '__main__':
    lst = list()
    unit_lst = [UnitCreator.create_unit(unit="MARINE"),
                UnitCreator.create_unit(unit="FIREBAT"),
                UnitCreator.create_unit(unit="WRIGHT"),
                UnitCreator.create_unit(unit="BATTLECRUISER"),
                UnitCreator.create_unit(unit="TRANSPORTER"),
                UnitCreator.create_unit(unit="WARSHIP")]

    for item in unit_lst:
        print(item)
        item.move()
        item.attack()
