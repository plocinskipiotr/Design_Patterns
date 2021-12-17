"""
Light bulb
"""


class LightBulb():
    """Light bulb class"""

    def __init__(self, state):
        self._state = state

    def turn_on(self):
        """Turning on"""
        self._state = True

    def turn_off(self):
        """Turning off"""
        self._state = False

    def click(self):
        """Chaning the state to opposite"""
        self._state = not self._state

    def set_state(self, state):
        """Defining direct state"""
        self._state = state

    def __str__(self):
        if self._state:
            return "Bulb turned on"

        return "Bulb turned off"
