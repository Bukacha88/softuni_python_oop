from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances.appliance import Appliance


class Laptop(Appliance):
    COST = 1

    def __init__(self):
        super().__init__(cost=Laptop.COST)
