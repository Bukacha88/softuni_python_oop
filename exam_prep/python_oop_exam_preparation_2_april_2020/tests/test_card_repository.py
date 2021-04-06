from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import CardRepository
from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import MagicCard


class TestCardRepository(TestCase):
    def test_card_repository__init__(self):
        card_repository = CardRepository()
        self.assertEqual(0, card_repository.count)
        self.assertEqual([], card_repository.cards)

    def test_card_repository__add__when_successful(self):
        card_repository = CardRepository()
        card = MagicCard('test name')
        card_repository.add(card)
        self.assertEqual([card], card_repository.cards)
        self.assertEqual(1, card_repository.count)

    def test_card_repository__add__when_unsuccessful(self):
        card_repository = CardRepository()
        card = MagicCard('test name')
        card_repository.add(card)
        card_1 = MagicCard('test name')
        with self.assertRaises(ValueError) as context:
            card_repository.add(card_1)
        self.assertEqual("Card test name already exists!", str(context.exception))

    def test_card_repository__remove__when_successful(self):
        card_repository = CardRepository()
        card = MagicCard('test name')
        card_repository.add(card)
        card_repository.remove('test name')
        self.assertEqual([], card_repository.cards)
        self.assertEqual(0, card_repository.count)

    def test_card_repository__remove__when_unsuccessful(self):
        card_repository = CardRepository()
        card = MagicCard('test name')
        card_repository.add(card)
        with self.assertRaises(ValueError) as context:
            card_repository.remove('')
        self.assertEqual("Card cannot be an empty string!", str(context.exception))

    def test_card_repository__find__method(self):
        card_repository = CardRepository()
        card = MagicCard('test name')
        card_repository.add(card)
        card_to_find = card_repository.find('test name')
        self.assertEqual(card, card_to_find)