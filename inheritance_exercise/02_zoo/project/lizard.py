from exam_prep.python_oop_exam_16_aug_2020.project import Reptile


class Lizard(Reptile):
    def __init__(self, name):
        Reptile.__init__(self, name)


