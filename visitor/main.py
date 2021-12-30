"""
Main loop for visitor example
"""

import visitor
import element

if __name__ == '__main__':
    pass
    v = visitor.Visitor()
    el_a = element.ElementA()
    el_b = element.ElementB()
    el_c = element.ElementC()
    el_a2 = element.ElementA()
    el_a3 = element.ElementA()
    el_b2 = element.ElementB()

    lst = [el_a, el_b, el_c, el_a2, el_a3, el_b2]

    for item in lst:
        item.accept(v)

    print(v)
