"""
Main loop for composite example
"""

from soldier import Soldier
from squad import Squad
from platoon import Platoon

if __name__ == '__main__':
    Mark = Soldier('Mark', 'Nowak', 'Private')
    Thomas = Soldier('Thomas', 'Neumann', 'Private')
    Jeff = Soldier('Jeff', 'Stevens', 'Private')
    Jops = Soldier('Jops', 'Jobs', 'Private')
    Mark.become_order()

    squad_1 = [Mark, Thomas, Jops, Jeff]
    squad_2 = [Thomas, Mark, Jeff, Jops]
    squad_3 = [Jeff, Thomas, Mark, Jops]

    SquadInstance_1 = Squad(squad_1)
    SquadInstance_2 = Squad(squad_2)
    SquadInstance_3 = Squad(squad_3)

    SquadInstance_1.become_order()

    PlatoonInstance_1 = Platoon([SquadInstance_1, SquadInstance_2, SquadInstance_3])

    PlatoonInstance_1.become_order()
