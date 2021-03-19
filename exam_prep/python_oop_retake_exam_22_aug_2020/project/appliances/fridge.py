from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances import Appliance


class Fridge(Appliance):
    COST = 1.2

    def __init__(self):
        super().__init__(cost=Fridge.COST)