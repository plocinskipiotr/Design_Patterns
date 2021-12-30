"""
Marine class
"""

from iprototype import IPrototype


class Marine(IPrototype):
    """Marine class"""

    def __init__(self, **stats):
        """Marine constructor method"""
        self.name = stats.get('name', 'MARINE')
        self.hp = stats.get('hp', 50)
        self.dmg = stats.get('dmg', 6)
        self.medals = stats.get('medals', ['private'])

    def clone(self):
        """Cloning method for Marine class"""
        stats = dict()
        stats['name'] = self.name
        stats['hp'] = self.hp
        stats['dmg'] = self.dmg
        stats['medals'] = self.medals
        return Marine(**stats)

    def __str__(self):
        """String representation of object"""
        return "{0} with hp: {1} dmg: {2} and medals: {3}".format(
            self.name, self.hp, self.dmg, self.medals)
