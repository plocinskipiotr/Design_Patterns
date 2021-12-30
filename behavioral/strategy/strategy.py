"""Sorting strategy"""

from istrategy import IStrategy


class AscSorting(IStrategy):
    """Ascending sorting strategy"""

    def execute(self, data):
        return self._asc_sorting(data)

    @staticmethod
    def _asc_sorting(data: list):
        """Ascending sorting"""
        data.sort()


class DescSorting(IStrategy):
    """Descending sorting strategy"""

    def execute(self, data):
        return self._desc_sorting(data)

    @staticmethod
    def _desc_sorting(data: list):
        """Descending sorting"""
        data.sort(reverse=True)
