from exam_prep.exam_10_april_2021.project.decoration import BaseDecoration


class Plant(BaseDecoration):
    def __init__(self):
        super().__init__(comfort=5, price=10)