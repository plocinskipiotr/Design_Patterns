"""Context"""

from drink import Empty
from idrink import IDrink


class Bottle(IDrink):
    """Bottle class"""

    def __init__(self, state: IDrink = Empty):
        self.state = state

    def change_state(self, state):
        """Changing bottle state"""
        self.state = state

    def drink(self):
        self.state = self.state.drink()

    def fill(self):
        self.state = self.state.fill()
