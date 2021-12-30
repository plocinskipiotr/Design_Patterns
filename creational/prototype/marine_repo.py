"""
Marin repository, from there marines could be immediately cloned
"""

from marine import Marine
from marine_cfg import STRONG_MARINE, MEDIUM_MARINE, WEAK_MARINE

MARINE_REPO = {
    "STRONG_MARINE": Marine(**STRONG_MARINE),
    "STANDARD MARINE": Marine(),
    "MEDIUM_MARINE": Marine(**MEDIUM_MARINE),
    "WEAK_MARINE": Marine(**WEAK_MARINE)
}
