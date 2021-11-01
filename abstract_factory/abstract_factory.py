"""Abstract units factory"""
from iunit_factory import IUnitFactory
from fly_unit_factory import FlyUnitCreator
from sea_unit_factory import SeaUnitCreator
from land_unit_factory import LandUnitCreator


class UnitCreator():
    """Abstract Factory method"""

    @staticmethod
    def create_unit(**kwargs):
        """Creating unit from concrete factory"""
        unit = kwargs.get("unit")
        if unit in FlyUnitCreator.FLYUNITS:
            return FlyUnitCreator.create_unit(unit)
        if unit in LandUnitCreator.LANDUNITS:
            return LandUnitCreator.create_unit(unit)
        if unit in SeaUnitCreator.SEAUNITS:
            return SeaUnitCreator.create_unit(unit)
        raise AttributeError("There is no such unit: " + unit + " to create")
