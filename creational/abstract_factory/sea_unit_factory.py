"""Sea units factory"""
from sea_unit import Transporter, Warship
from iunit_factory import IUnitFactory


class SeaUnitCreator(IUnitFactory):
    """Sea unit factory"""

    @staticmethod
    def create_unit(unit):
        """Factory method"""
        if unit == "TRANSPORTER":
            return Transporter()
        if unit == "WARSHIP":
            return Warship()
        raise ValueError("There is no such unit: " + unit)

    SEAUNITS = {"TRANSPORTER", "WARSHIP"}
