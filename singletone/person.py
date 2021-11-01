class Person():
    _instance = None

    @staticmethod
    def get_instance():
        if Person._instance is None:
            Person("Default Name", "Default Surname")
        return Person._instance

    def __init__(self, name, surname):
        if Person._instance != None:
            raise Exception("Singleton cannot be instantiated, use get_instance instead")
        else:
            self.name = name
            self.surname = surname
            Person._instance = self

    def modify(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname
