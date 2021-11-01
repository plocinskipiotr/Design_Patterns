from person import Person

if __name__ == '__main__':
    s0 = Person.get_instance()
    s0.modify("Dave", "Davis")
    s1 = Person.get_instance()
    s2 = Person.get_instance()

    if s1 is not s2 is not s0:
        print("ERROR")

    print(s0, s1, s2)

    s2.modify("Thomas", "Neuer")

    if s1 is not s2 is not s0:
        print("ERROR")

    print(s0, s1, s2)
