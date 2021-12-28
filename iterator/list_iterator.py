"""
List iterator implementation
"""

from iiterator import IIterator


class BasicIterator(IIterator):
    """Custom list iterator implementations"""

    def __init__(self, lst):
        self._lst = lst
        self._index = 0

    def get_next(self):
        """Get next element from list"""
        if self.has_more():
            result = self._lst[self._index]
            self._index += 1
            return result
        return None

    def has_more(self) -> bool:
        """Check if list contains more elements"""
        try:
            result = self._lst[self._index]
        except IndexError:
            return False
        return True

    def __str__(self):
        try:
            return "current index,element: " + \
                   '(' + str(self._index) + ',' + str(self._lst[self._index]) + ')'
        except IndexError:
            return "list index out of range"


class FilteringIterator(IIterator):
    """Custom list iterator implementations"""

    def __init__(self, lst, custom_filter):
        self._lst = lst
        self._index = 0
        self._filter = custom_filter

    def get_next(self):
        """Get next element from list"""
        while True:
            try:
                result = self._lst[self._index]
                if result > self._filter:
                    self._index = self._find_next()
                    return result
                self._index += 1
            except IndexError:
                return None

    def _find_next(self):
        """Iterate to next element in list, takes filter into account"""
        self._index += 1
        while True:
            try:
                result = self._lst[self._index]
                if result > self._filter:
                    return self._index
                self._index += 1
            except IndexError:
                return self._index

    def has_more(self) -> bool:
        """Check if list contains more elements, takes filter into account"""
        index = self._index
        while True:
            try:
                result = self._lst[index]
                if result > self._filter:
                    return True
                index += 1
            except IndexError:
                return False

    def __str__(self):
        try:
            return "current index,element: " + \
                   '(' + str(self._index) + ',' + str(self._lst[self._index]) + ')'
        except IndexError:
            return "list index out of range"
