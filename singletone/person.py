class Person():
    _instance = None

    @staticmethod
    def get_instance():
        if Person._instance is None:
            Person("Default Name", "Default Surname")
        return Person._instance

    def __init__(self, name, surname):
        if Person._instance != None:
            raise Exception("Singleton cannot be instantiated")
        else:
            self.name = name
            self.surname = surname
            Person._instance = self
