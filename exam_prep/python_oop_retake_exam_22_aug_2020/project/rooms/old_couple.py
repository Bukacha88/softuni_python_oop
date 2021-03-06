from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances.fridge import Fridge
from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances.stove import Stove
from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances.tv import TV
from exam_prep.python_oop_retake_exam_22_aug_2020.project.rooms.room import Room


class OldCouple(Room):

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, budget=pension_one+pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)