"""Context"""

from istrategy import IStrategy
from strategy import AscSorting


class Context():
    """Context class"""

    def __init__(self, strategy: IStrategy = AscSorting()):
        self._strategy = strategy

    def set_strategy(self, strategy: IStrategy):
        """Set strategy"""
        self._strategy = strategy

    def execute_strategy(self, data: list):
        """Execute strategy"""
        self._strategy.execute(data)
