"""Abstract class"""

from abc import ABCMeta


class AbstractClass(metaclass=ABCMeta):
    """Abstract template class"""
    def template_method(self):
        """Template method"""
        self.step_1()
        self.step_2()
        self.step_3()

    @staticmethod
    def step_1():
        """Abstract step of algorithm"""
        print('abstract step_1')


    @staticmethod
    def step_2():
        """Abstract step of algorithm"""
        print('abstract step_2')

    @staticmethod
    def step_3():
        """Abstract step of algorithm"""
        print('abstract step_3')
