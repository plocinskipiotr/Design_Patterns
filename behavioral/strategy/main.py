"""
Main loop for strategy example
"""

from strategy import AscSorting, DescSorting
from context import Context

if __name__ == '__main__':
    c = Context()
    data = [1, 2, 1, 3, 1, 4, 1, 5]

    c.execute_strategy(data)
    print(data)

    c.set_strategy(DescSorting())
    c.execute_strategy(data)
    print(data)

    c.set_strategy(AscSorting())
    c.execute_strategy(data)
    print(data)
