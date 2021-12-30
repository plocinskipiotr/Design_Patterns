"""
Main loop for template method example
"""

from abstract_class import AbstractClass
from concrete_class import ConcreteClass

if __name__ == '__main__':
    a = AbstractClass()
    a.template_method()
    b = ConcreteClass()
    b.template_method()
