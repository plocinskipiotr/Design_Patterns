from abc import ABC, abstractmethod


class IStudentBuilder(ABC):
    """The IStudentBuilder Interface"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def with_name(self, name):
        pass

    @abstractmethod
    def with_surename(self, name):
        pass

    @abstractmethod
    def with_age(self, age):
        pass

    @abstractmethod
    def get_result(self):
        pass
