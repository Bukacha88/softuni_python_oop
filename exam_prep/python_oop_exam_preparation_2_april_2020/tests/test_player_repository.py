from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.player_repository import PlayerRepository
from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.beginner import Beginner


class TestPlayerRepository(TestCase):
    def test_player_repository__init__(self):
        player_repository = PlayerRepository()
        self.assertEqual(0, player_repository.count)
        self.assertEqual([], player_repository.players)

    def test_player_repository__add__when_successful(self):
        player_repository = PlayerRepository()
        player = Beginner('test name')
        player_repository.add(player)
        self.assertEqual([player], player_repository.players)
        self.assertEqual(1, player_repository.count)

    def test_player_repository__add__when_unsuccessful(self):
        player_repository = PlayerRepository()
        player = Beginner('test name')
        player_repository.add(player)
        player_1 = Beginner('test name')
        with self.assertRaises(ValueError) as context:
            player_repository.add(player_1)
        self.assertEqual("Player test name already exists!", str(context.exception))

    def test_player_repository__remove__when_successful(self):
        player_repository = PlayerRepository()
        player = Beginner('test name')
        player_repository.add(player)
        player_repository.remove('test name')
        self.assertEqual([], player_repository.players)
        self.assertEqual(0, player_repository.count)

    def test_player_repository__remove__when_unsuccessful(self):
        player_repository = PlayerRepository()
        player = Beginner('test name')
        player_repository.add(player)
        with self.assertRaises(ValueError) as context:
            player_repository.remove('')
        self.assertEqual("Player cannot be an empty string!", str(context.exception))

    def test_player_repository__find__method(self):
        player_repository = PlayerRepository()
        player = Beginner('test name')
        player_repository.add(player)
        player_to_find = player_repository.find('test name')
        self.assertEqual(player, player_to_find)