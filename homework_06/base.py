from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight=1400, started=False, fuel=60, fuel_consumption=8):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            print('Vehicle already started')
            return
        if self.fuel > 0:
            self.started = True
            print('Vehicle started')
            return
        raise LowFuelError('Low level fuel')

    def move(self, distance):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
            return
        raise NotEnoughFuel('Not enough fuel')