"""
Mediator implementation
"""
from typing import Union
from imediator import IMediator
from vehicle_enum import VehicleState
from bus import Bus
from car import Car


class Mediator(IMediator):
    """Mediator class"""

    def __init__(self):
        self.cars = list()
        self.buses = list()

    def add(self, vehicle: Union[Bus, Car]):
        """Adding vehicle to car/bus container"""
        if isinstance(vehicle, Car):
            self.cars.append(vehicle)
        if isinstance(vehicle, Bus):
            self.buses.append(vehicle)

    def notify(self, sender: Union[Bus, Car]):
        if isinstance(sender, Car) and sender.state == VehicleState.HOLD:
            for bus in self.buses:
                bus.state = VehicleState.RUN
            for car in self.cars:
                car.state = VehicleState.HOLD

        if isinstance(sender, Car) and sender.state == VehicleState.RUN:
            for bus in self.buses:
                bus.state = VehicleState.HOLD
            for car in self.cars:
                car.state = VehicleState.RUN

        if isinstance(sender, Bus) and sender.state == VehicleState.HOLD:
            for car in self.cars:
                car.state = VehicleState.RUN
            for bus in self.buses:
                bus.state = VehicleState.HOLD

        if isinstance(sender, Bus) and sender.state == VehicleState.RUN:
            for car in self.cars:
                car.state = VehicleState.HOLD
            for bus in self.buses:
                bus.state = VehicleState.RUN
