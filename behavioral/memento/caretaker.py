"""Caretaker"""
from memento import Memento


class Caretaker():
    """Caretaker class"""

    def __init__(self, bottle):
        self.bottle = bottle
        self.history: list[Memento] = list()

    def save_snapshot(self):
        """Saving bottle snapshot"""
        snap = self.bottle.save()
        self.history.append(snap)

    def restore_snapshot(self):
        """Restoring bottle snapshot"""
        if self.history:
            snap = self.history.pop()
            self.bottle.restore(snap)
