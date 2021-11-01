from person import Person

if __name__ == '__main__':
    s0 = Person.get_instance()
    s1 = Person.get_instance()
    s2 = Person.get_instance()

    if s1 is not s2 is not s0:
        print("ERROR")

