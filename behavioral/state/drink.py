"""Drink states"""
from idrink import IDrink


class Full(IDrink):
    """State"""

    @staticmethod
    def fill() -> IDrink:
        print("Fill cannot be executed: Bottle is full")
        return Full()

    @staticmethod
    def drink() -> IDrink:
        print("Drink executed: Bottle is now half full")
        return Half()


class Half(IDrink):
    """State"""

    @staticmethod
    def fill() -> IDrink:
        print("Fill executed: Bottle is full")
        return Full()

    @staticmethod
    def drink() -> IDrink:
        print("Drink executed: Bottle is now empty")
        return Empty()


class Empty(IDrink):
    """State"""

    @staticmethod
    def fill() -> IDrink:
        print("Fill executed: Bottle is half full")
        return Half()

    @staticmethod
    def drink() -> IDrink:
        print("Drink cannot be executed: Bottle is empty")
        return Empty()
