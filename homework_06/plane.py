"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_06.base import Vehicle
from homework_06.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        super().__init__(max_cargo)
        self.cargo = cargo

    def load_cargo(self, new_cargo):
        if new_cargo + self.cargo > self.weight:
            raise CargoOverload
        self.cargo = new_cargo + self.cargo

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo