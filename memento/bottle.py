"""Bottle class"""

from states import BottleStates
from memento import Memento


class Bottle():
    """Bottle class"""

    def __init__(self, state=BottleStates.FULL):
        self.state = state

    def drink(self):
        """Drinking from bottle"""
        if self.state == BottleStates.FULL:
            self.state = BottleStates.HALF
        elif self.state == BottleStates.HALF:
            self.state = BottleStates.EMPTY
        else:
            self.state = BottleStates.EMPTY

    def save(self) -> Memento:
        """Saving bottle state to memento"""
        return Memento(self.state)

    def restore(self, mem: Memento):
        """Restoring bottle state from memento"""
        self.state = mem.get_state()

    def __str__(self):
        return 'bottle state: ' + str(self.state)
