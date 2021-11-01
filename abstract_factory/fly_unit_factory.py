"""Flying units factory"""
from fly_unit import Wright, Battlecruiser
from iunit_factory import IUnitFactory


class FlyUnitCreator(IUnitFactory):
    """Flying unit factory"""

    @staticmethod
    def create_unit(unit: str):
        """Factory method"""
        if unit == "WRIGHT":
            return Wright()
        if unit == "BATTLECRUISER":
            return Battlecruiser()
        raise ValueError("There is no such unit: " + unit)

    FLYUNITS = {"BATTLECRUISER", "WRIGHT"}
