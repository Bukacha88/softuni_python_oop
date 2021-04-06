from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.beginner import Beginner


class TestBeginner(TestCase):
    def setUp(self):
        self.beginner = Beginner('Hulk')

    def test_beginner__init__(self):
        self.assertEqual('Hulk', self.beginner.username)
        self.assertEqual(50, self.beginner.health)
        self.assertEqual(0, self.beginner.card_repository.count)
        self.assertEqual([], self.beginner.card_repository.cards)

    def test_beginner__when_health_is_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.beginner.health = -10
            self.assertEqual(True, self.beginner.is_dead)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(context.exception))

    def test_beginner__when_damage_points_less_than_zero(self):
        msg = 'Damage points cannot be less than zero.'
        with self.assertRaises(ValueError) as context:
            self.beginner.take_damage(-10)
        self.assertEqual(msg, str(context.exception))

    def test_beginner__when_empty_string_is_given(self):
        msg = "Player's username cannot be an empty string."
        player = ''
        with self.assertRaises(ValueError) as context:
            Beginner(player)
        self.assertEqual(msg, str(context.exception))

    def test_beginner__when_take_damage_positive_but_kills_hero(self):
        msg = "Player's health bonus cannot be less than zero."
        with self.assertRaises(ValueError) as context:
            self.beginner.take_damage(260)
        self.assertEqual(msg, str(context.exception))

