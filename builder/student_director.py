from student_builder import StudentBuilder


class AGradeStudentDirector:
    """The Director, building Student with excellent grades"""

    @staticmethod
    def construct():
        """Constructor method"""
        return StudentBuilder() \
            .with_name('Max') \
            .with_surename('Kowalski') \
            .with_age(22) \
            .with_mean(5.0) \
            .get_result()


class BGradeStudentDirector:
    """The Director, building Student with very good grades"""

    @staticmethod
    def construct():
        """Constructor method"""
        return StudentBuilder() \
            .with_name('Antoni') \
            .with_surename('Nowak') \
            .with_age(22) \
            .with_mean(4.0) \
            .get_result()


class CGradeStudentDirector:
    """The Director, building Student with good grades"""

    @staticmethod
    def construct():
        """Constructor method"""
        return StudentBuilder() \
            .with_name('Vincent') \
            .with_surename('Schroeder') \
            .with_age(22) \
            .with_mean(3.0) \
            .get_result()


class DGradeStudentDirector:
    """The Director, building Student with bad grades"""

    @staticmethod
    def construct():
        """Constructor method"""
        return StudentBuilder() \
            .with_name('Mark') \
            .with_surename('Zuecker') \
            .with_age(22) \
            .with_mean(2.0) \
            .get_result()
