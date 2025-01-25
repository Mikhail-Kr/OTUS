"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_06.base import Vehicle
from homework_06.engine import Engine


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine