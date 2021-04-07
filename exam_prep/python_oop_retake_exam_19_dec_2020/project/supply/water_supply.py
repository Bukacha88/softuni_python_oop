from exam_prep.python_oop_retake_exam_19_dec_2020.project import Supply


class WaterSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=40)