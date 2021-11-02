"""
Main loop for prototype example
"""

from marine import Marine
from marine_repo import MARINE_REPO

if __name__ == '__main__':
    marine = Marine()

    lst = [marine, marine.clone()]

    for item in lst:
        print(item)

    strong_marine_clone = MARINE_REPO.get("STRONG_MARINE").clone()
    medium_marine_clone = MARINE_REPO.get("MEDIUM_MARINE").clone()
    weak_marine_clone = MARINE_REPO.get("WEAK_MARINE").clone()

    lst = [strong_marine_clone, medium_marine_clone, weak_marine_clone]
    for item in lst:
        print(item)
