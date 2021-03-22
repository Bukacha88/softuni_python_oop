from exam_prep.python_oop_exam_16_aug_2020.project import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Power', int(capacity * 0.25), int(1.75 * memory))