"""
Main loop for memento example
"""
from bottle import Bottle
from caretaker import Caretaker

if __name__ == '__main__':
    bottle = Bottle()
    c = Caretaker(bottle)
    c.save_snapshot()

    bottle.drink()
    print(bottle)

    c.save_snapshot()

    bottle.drink()
    print(bottle)

    c.restore_snapshot()

    print(bottle)

    c.restore_snapshot()

    print(bottle)
