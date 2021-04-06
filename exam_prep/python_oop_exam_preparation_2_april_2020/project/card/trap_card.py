from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import Card


class TrapCard(Card):

    def __init__(self, name):
        super().__init__(name, damage_points=120, health_points=5)