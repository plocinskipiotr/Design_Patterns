"""
Marine classes
Now there are:
Marine class
LowSkilledMarine subclass
MediumSkilledMarine subclass
HighSkilledMarine subclass
"""
from factory.irange_unit import IRangeUnit


class Marine(IRangeUnit):
    """UAC Marine"""

    def __init__(self, name='Marine', hp=0, dmg=0, range=0):
        """Constructor"""
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.range = range

    def __str__(self):
        """String representation"""
        return 'type: {0}\nhp: {1}\ndamage: {2}\n' \
               'range: {3}' \
            .format(self.name, self.hp, self.dmg, self.range)


class LowSkilledMarine(Marine):
    """Low skilled marine"""

    def __init__(self):
        """Constructor"""
        super().__init__(
            name='LowSkilledMarine',
            hp=50,
            dmg=6,
            range=10)

    def shoot(self):
        """Shooting"""
        print("Unaimed shooting")


class MediumSkilledMarine(Marine):
    """Medium skilled marine"""

    def __init__(self):
        super().__init__(
            name='MediumSkilledMarine',
            hp=60,
            dmg=8,
            range=12)

    def shoot(self):
        """Shooting"""
        print("Aimed shooting")


class HighSkilledMarine(Marine):
    """High skilled marine"""

    def __init__(self):
        super().__init__(
            name='HighSkilledMarine',
            hp=80,
            dmg=10,
            range=15,
        )

    def shoot(self):
        """Shooting"""
        print("Superb shooting")
