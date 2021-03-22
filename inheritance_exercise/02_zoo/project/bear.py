from exam_prep.python_oop_exam_16_aug_2020.project import Mammal


class Bear(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)

