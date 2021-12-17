"""
Main loop for command example
"""

from receiver import LightBulb
from commands import TurnOff, TurnOn, Click
from invoker import Invoker

if __name__ == '__main__':
    invoker = Invoker()
    bulb = LightBulb(state=False)
    turn_on = TurnOn(bulb)
    turn_off = TurnOff(bulb)
    click = Click(bulb)

    print(bulb)
    invoker.add_command(turn_on, turn_off, click)

    invoker.execute_command()
    print(bulb)
    invoker.execute_command()
    print(bulb)
    invoker.execute_command()
    print(bulb)
    invoker.unexecute_command()
    print(bulb)
    invoker.unexecute_command()
    print(bulb)
    invoker.unexecute_command()
    print(bulb)
