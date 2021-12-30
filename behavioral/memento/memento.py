"""Memento class"""

class Memento():
    """Memento class"""

    def __init__(self, state):
        self.state = state

    def get_state(self):
        """Get object state"""
        return self.state
