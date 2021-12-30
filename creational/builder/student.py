class Student():
    """The Student"""

    def __init__(self, name='', surname='', age=0, mean=0.0):
        """Student constructor"""
        self.name = name
        self.surname = surname
        self.age = age
        self.mean = mean

    def __str__(self):
        """Student string representation"""
        return 'name: {0}\nsurename: {1}\nage: {2}\nmean: {3}' \
            .format(self.name, self.surname, self.age, self.mean)
