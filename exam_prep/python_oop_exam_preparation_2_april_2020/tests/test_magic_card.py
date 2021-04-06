from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import MagicCard


class TestMagicCard(TestCase):
    def setUp(self):
        self.magic_card = MagicCard('test name')

    def test_magic_card__init(self):
        self.assertEqual('test name', self.magic_card.name)
        self.assertEqual(5, self.magic_card.damage_points)
        self.assertEqual(80, self.magic_card.health_points)

    def test_magic_card__when_name_empty_string(self):
        msg = "Card's name cannot be an empty string."
        card = ''
        with self.assertRaises(ValueError) as context:
            MagicCard(card)

        self.assertEqual(msg, str(context.exception))

    def test_magic_card__when_health_less_than_0(self):
        msg = "Card's HP cannot be less than zero."
        with self.assertRaises(ValueError) as context:
            self.magic_card.health_points = -10
        self.assertEqual(msg, str(context.exception))

    def test_magic_card__when_damage_points_less_than_0(self):
        msg = "Card's damage points cannot be less than zero."
        with self.assertRaises(ValueError) as context:
            self.magic_card.damage_points = -10
        self.assertEqual(msg, str(context.exception))