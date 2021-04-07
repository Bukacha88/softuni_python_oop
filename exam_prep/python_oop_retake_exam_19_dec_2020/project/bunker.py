from exam_prep.python_oop_retake_exam_19_dec_2020.project.medicine import Painkiller
from exam_prep.python_oop_retake_exam_19_dec_2020.project.medicine import Salve
from exam_prep.python_oop_retake_exam_19_dec_2020.project.supply.food_supply import FoodSupply
from exam_prep.python_oop_retake_exam_19_dec_2020.project import WaterSupply


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_objects = [obj for obj in self.supplies if isinstance(obj, FoodSupply)]
        if not food_objects:
            raise IndexError("There are no food supplies left!")
        return food_objects

    @property
    def water(self):
        water_objects = [obj for obj in self.supplies if isinstance(obj, WaterSupply)]
        if not water_objects:
            raise IndexError("There are no water supplies left!")
        return water_objects

    @property
    def painkillers(self):
        painkiller_objects = [obj for obj in self.medicine if isinstance(obj, Painkiller)]
        if not painkiller_objects:
            raise IndexError("There are no painkillers left!")
        return painkiller_objects

    @property
    def salves(self):
        salves_objects = [obj for obj in self.medicine if isinstance(obj, Salve)]
        if not salves_objects:
            raise IndexError("There are no salves left!")
        return salves_objects

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if med.__class__.__name__ == medicine_type:
                    med.apply(survivor)
                    self.medicine.remove(med)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for supp in self.supplies[::-1]:
                if supp.__class__.__name__ == sustenance_type:
                    supp.apply(survivor)
                    self.supplies.remove(supp)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            FoodSupply().apply(survivor)
            WaterSupply().apply(survivor)