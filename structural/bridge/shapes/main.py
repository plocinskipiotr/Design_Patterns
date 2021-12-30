"""
Main loop for bridge example
"""

from square import Square
from circle import Circle
from blue import Blue
from red import Red

if __name__ == '__main__':
    RedSquare = Square(10, Red())
    BlueSquare = Square(10, Blue())
    RedCircle = Circle(4, Red())
    BlueCircle = Circle(4, Blue())

    print(RedSquare, BlueSquare, RedCircle, BlueCircle)
