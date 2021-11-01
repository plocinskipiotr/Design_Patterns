"""
Main loop for factory example
"""

from marine_creator import CreateMarine
from marine_creator import EnumMarine

if __name__ == '__main__':
    marine = CreateMarine.create()
    marine_none = CreateMarine.create(marine_type=None)
    marine_low = CreateMarine.create(marine_type=EnumMarine.LOW)
    marine_med = CreateMarine.create(marine_type=EnumMarine.MED)
    marine_high = CreateMarine.create(marine_type=EnumMarine.HIGH)

    marine_lst = [marine, marine_none, marine_low, marine_med, marine_high]
    for soldier in marine_lst:
        print(soldier)
