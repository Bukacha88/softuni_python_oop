from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances import Appliance


class Stove(Appliance):
    COST = 0.7

    def __init__(self):
        super().__init__(cost=Stove.COST)