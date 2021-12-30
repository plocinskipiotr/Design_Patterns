"""
Main loop for state example
"""

from bottle import Bottle
from drink import Half

if __name__ == '__main__':
    bottle = Bottle()

    bottle.drink()

    bottle.fill()
    bottle.fill()
    bottle.fill()

    bottle.drink()
    bottle.drink()
    bottle.drink()

    bottle.fill()

    bottle.drink()

    bottle.change_state(Half)
    bottle.drink()
    bottle.drink()
