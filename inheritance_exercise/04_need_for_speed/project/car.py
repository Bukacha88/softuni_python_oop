from exam_prep.python_oop_exam_16_aug_2020.project import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = Car.DEFAULT_FUEL_CONSUMPTION
