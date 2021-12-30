"""
Factory method for marine classes
"""

from enum import Enum, auto

from icreator import ICreator
from marine import LowSkilledMarine, MediumSkilledMarine, HighSkilledMarine


class EnumMarine(Enum):
    """Marine types for factory use"""
    LOW = auto()
    MED = auto()
    HIGH = auto()


class CreateMarine(ICreator):
    """Marine factory"""

    @staticmethod
    def create(**kwargs):
        """Marine factory method"""
        marine_type = kwargs.get("marine_type", EnumMarine.LOW)
        try:
            if marine_type == marine_type.LOW:
                return LowSkilledMarine()
            elif marine_type == marine_type.MED:
                return MediumSkilledMarine()
            elif marine_type == marine_type.HIGH:
                return HighSkilledMarine()
        except AttributeError:
            return LowSkilledMarine()
