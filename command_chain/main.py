"""
Main loop for command chain example
"""

from armory_handle import ArmoryHandle
from first_aid_handle import FirstAidHandle
from food_handle import FoodHandle
from base_handle import BaseHandler

if __name__ == '__main__':
    UNARMED_REQUEST = "isUnarmed"
    WOUND_REQUEST = "isWounded"
    HUNGRY_REQUEST = "isHungry"
    DEAD_REQUEST = "isDead"

    base_handler = BaseHandler()
    weapon_handler = ArmoryHandle()
    food_handler = FoodHandle()
    first_aid_handler = FirstAidHandle()

    base_handler.set_next(weapon_handler)
    weapon_handler.set_next(food_handler)
    food_handler.set_next(first_aid_handler)

    base_handler.handle(UNARMED_REQUEST)
    base_handler.handle(WOUND_REQUEST)
    base_handler.handle(HUNGRY_REQUEST)
    base_handler.handle(DEAD_REQUEST)
