"""
Singleton Person class
"""


class Person():
    """Singleton"""
    _instance = None

    @staticmethod
    def get_instance():
        """Get instance of Person"""
        if Person._instance is None:
            Person("Name", "Surname")
        return Person._instance

    def __init__(self, name, surname):
        """
            Constructor class with default values
            Saving class instance to private parameter _instance
        """
        if Person._instance is not None:
            raise Exception("Singleton cannot be instantiated, use get_instance instead")

        self.name = name
        self.surname = surname
        Person._instance = self

    def modify(self, name, surname):
        """Modify object fields"""
        self.name = name
        self.surname = surname

    def __str__(self):
        """String representation of object"""
        return self.name + " " + self.surname
