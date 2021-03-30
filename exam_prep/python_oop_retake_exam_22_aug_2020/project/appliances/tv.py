from exam_prep.python_oop_retake_exam_22_aug_2020.project.appliances.appliance import Appliance


class TV(Appliance):
    COST = 1.5

    def __init__(self):
        super().__init__(cost=TV.COST)