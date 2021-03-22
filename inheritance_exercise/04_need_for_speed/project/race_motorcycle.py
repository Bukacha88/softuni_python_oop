from exam_prep.python_oop_exam_16_aug_2020.project import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION

