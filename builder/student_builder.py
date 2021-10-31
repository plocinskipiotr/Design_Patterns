from istudent_builder import IStudentBuilder
from student import Student


class StudentBuilder(IStudentBuilder):
    """Builder for Student class"""


    def __init__(self):
        """StudentBuilder constructor"""
        self.student = Student()


    def with_name(self, name):
        """Set the name of Student"""
        self.student.name = name
        return self


    def with_surename(self, name):
        """Set the surname of Student"""
        self.student.surname = name
        return self


    def with_age(self, age):
        """Set the age of Student"""
        self.student.age = age
        return self


    def with_mean(self, mean):
        """Set the mean of Student"""
        self.student.mean = mean
        return self


    def get_result(self):
        """Return Student"""
        return self.student
