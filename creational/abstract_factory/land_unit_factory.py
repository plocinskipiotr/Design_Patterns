"""Land units factory"""
from land_unit import Marine, Firebat
from iunit_factory import IUnitFactory


class LandUnitCreator(IUnitFactory):
    """Land unit factory"""

    @staticmethod
    def create_unit(unit: str):
        """Factory method"""
        if unit == "MARINE":
            return Marine()
        if unit == "FIREBAT":
            return Firebat()
        raise ValueError("There is no such unit: " + unit)

    LANDUNITS = {"MARINE", "FIREBAT"}
