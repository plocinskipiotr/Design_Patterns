"""
Custom list implementation
"""

from iiterator import IIterator
from list_iterator import BasicIterator, FilteringIterator
from icollection import ICollection


class CustomList(ICollection):
    """Collection interface"""

    def __init__(self, lst: list):
        self.lst = lst
        self.filter = filter

    def create_iterator(self) -> IIterator:
        """Create standard iterator"""
        return BasicIterator(self.lst)

    def create_filtering_iterator(self, custom_filter) -> IIterator:
        """Create filtering iterator"""
        return FilteringIterator(self.lst, custom_filter)
