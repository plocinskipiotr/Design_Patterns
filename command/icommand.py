"""
Command interface
"""

from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    """Command interface"""

    @staticmethod
    @abstractmethod
    def execute():
        """Command execute method"""

    @staticmethod
    @abstractmethod
    def unexecute():
        """Command unexecute method"""
