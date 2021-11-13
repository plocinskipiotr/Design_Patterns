"""
Main loop for command chain example
"""

from armory_handle import ArmoryHandle
from first_aid_handle import FirstAidHandle
from food_handle import FoodHandle
from base_handle import BaseHandler

if __name__ == '__main__':
    unarmed_request = "isUnarmed"
    wound_request = "isWounded"
    hungry_request = "isHungry"
    dead_request = "isDead"

    base_handler = BaseHandler()
    weapon_handler = ArmoryHandle()
    food_handler = FoodHandle()
    first_aid_handler = FirstAidHandle()

    base_handler.set_next(weapon_handler)
    weapon_handler.set_next(food_handler)
    food_handler.set_next(first_aid_handler)

    base_handler.handle(unarmed_request)
    base_handler.handle(wound_request)
    base_handler.handle(hungry_request)
    base_handler.handle(dead_request)
