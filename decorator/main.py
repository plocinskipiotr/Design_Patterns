"""
Main loop for decorator example
"""

from fireman import Fireman
from masterfireman import MasterFireman

if __name__ == '__main__':
    FiremanInstance = Fireman('Stanislaw', 'Niklaus', 25)
    MasterFiremanInstance = MasterFireman('Tom', 'Hard', 30, FiremanInstance)

    print(FiremanInstance)
    print(MasterFiremanInstance)

    FiremanInstance.put_out_the_fire()
    MasterFiremanInstance.put_out_the_fire()
