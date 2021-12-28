"""
Mediator implementation
"""
from typing import Union
from imediator import IMediator
from vehicle_enum import VehicleState
from bus import Bus
from car import Car


class Mediator(IMediator):

    def __init__(self):
        self.cars = list()
        self.buses = list()

    def add(self, vehicle: Union[Bus, Car]):
        if type(vehicle) == Car:
            self.cars.append(vehicle)
        if type(vehicle) == Bus:
            self.buses.append(vehicle)

    def notify(self, sender: Union[Bus, Car]):
        if type(sender) == Car and sender.state == VehicleState.HOLD:
            for bus in self.buses:
                bus.state = VehicleState.RUN
            for car in self.cars:
                car.state = VehicleState.HOLD

        if type(sender) == Car and sender.state == VehicleState.RUN:
            for bus in self.buses:
                bus.state = VehicleState.HOLD
            for car in self.cars:
                car.state = VehicleState.RUN

        if type(sender) == Bus and sender.state == VehicleState.HOLD:
            for car in self.cars:
                car.state = VehicleState.RUN
            for bus in self.buses:
                bus.state = VehicleState.HOLD

        if type(sender) == Bus and sender.state == VehicleState.RUN:
            for car in self.cars:
                car.state = VehicleState.HOLD
            for bus in self.buses:
                bus.state = VehicleState.RUN
