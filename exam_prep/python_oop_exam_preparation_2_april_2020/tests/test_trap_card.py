from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import TrapCard


class TestTrapCard(TestCase):
    def setUp(self):
        self.trap_card = TrapCard('test name')

    def test_trap_card__init(self):
        self.assertEqual('test name', self.trap_card.name)
        self.assertEqual(120, self.trap_card.damage_points)
        self.assertEqual(5, self.trap_card.health_points)

    def test_trap_card__when_name_empty_string(self):
        msg = "Card's name cannot be an empty string."
        card = ''
        with self.assertRaises(ValueError) as context:
            TrapCard(card)

        self.assertEqual(msg, str(context.exception))

    def test_trap_card__when_health_less_than_0(self):
        msg = "Card's HP cannot be less than zero."
        with self.assertRaises(ValueError) as context:
            self.trap_card.health_points = -10
        self.assertEqual(msg, str(context.exception))

    def test_trap_card__when_damage_points_less_than_0(self):
        msg = "Card's damage points cannot be less than zero."
        with self.assertRaises(ValueError) as context:
            self.trap_card.damage_points = -10
        self.assertEqual(msg, str(context.exception))