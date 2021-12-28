"""
Bus
"""
from vehicle_enum import VehicleState
from vehicle import Vehicle


class Bus(Vehicle):

    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
        self.state = VehicleState.HOLD

    def __str__(self):
        return 'name: ' + self.name + ' state: ' + str(self.state)

    def stop(self):
        self.state = VehicleState.HOLD
        self.mediator.notify(self)
        print(self.name + ' stop')

    def start(self):
        self.state = VehicleState.RUN
        self.mediator.notify(self)
        print(self.name + ' start')