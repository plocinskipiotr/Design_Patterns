"""Generate Random Float Service"""
from random import Random
from iservice import IService


class RandomFloatService(IService):
    """Generate Random Float Service"""

    def get_data(self):
        """Generating random float from 0 to 10"""
        rand = Random()
        return int(rand.random() * 10) % 10
