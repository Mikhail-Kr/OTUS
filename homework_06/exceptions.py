"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotEnoughFuel(Exception):
    def __init__(self, message):
        super().__init__(message)

class CargoOverload(Exception):
    def __init__(self, message):
        super().__init__(message)
