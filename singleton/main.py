"""
Main loop for singleton example
"""

from person import Person

if __name__ == '__main__':
    s0 = Person.get_instance()
    print(s0)
    s0.modify("Dave", "Davis")
    s1 = Person.get_instance()
    s1.modify("Thomas", "Smith")
    s2 = Person.get_instance()

    if s0 is not s1 is not s2:
        raise Warning("Objects have not same ID")

    print(str(s0) + '\n' + str(s1) + '\n' + str(s2) + '\n')

    s2.modify("Thomas", "Neuer")

    if s0 is not s1 is not s2:
        raise Warning("Objects have not same ID")

    print(str(s0) + '\n' + str(s1) + '\n' + str(s2) + '\n')

    s3 = Person("exception", "throw")
