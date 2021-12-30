"""
Commands
"""

from receiver import LightBulb
from icommand import ICommand


class TurnOn(ICommand):
    """Turn on command"""

    def __init__(self, receiver, **kwargs):
        self._receiver: LightBulb = receiver
        self._name: str = "turn on"
        self._params = kwargs

    def execute(self):
        print('Executing command: ' + self._name)
        self._receiver.turn_on()

    def unexecute(self):
        print('Unexecuting command: ' + self._name)
        self._receiver.turn_off()


class TurnOff(ICommand):
    """Turn off command"""

    def __init__(self, receiver, **kwargs):
        self._receiver: LightBulb = receiver
        self._name: str = "turn off"
        self._params = kwargs

    def execute(self):
        print('Executing command: ' + self._name)
        self._receiver.turn_off()

    def unexecute(self):
        print('Unexecuting command: ' + self._name)
        self._receiver.turn_on()


class Click(ICommand):
    """Click command"""

    def __init__(self, receiver, **kwargs):
        self._receiver: LightBulb = receiver
        self._name: str = "click"
        self._params = kwargs

    def execute(self):
        print('Executing command: ' + self._name)
        self._receiver.click()

    def unexecute(self):
        print('Unexecuting command: ' + self._name)
        self._receiver.click()
