from exam_prep.python_oop_exam_16_aug_2020.project import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, 'Express', capacity_consumption, int(memory_consumption * 2))