import unittest

from exam_prep.python_oop_retake_exam_22_aug_2020.project.people.child import Child
from exam_prep.python_oop_retake_exam_22_aug_2020.project.rooms.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room('Peshovi', 100, 2)

    def test_room__init__expect_initialized(self):
        self.assertEqual('Peshovi', self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_room__expenses_setter__when_negative__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -3
        self.assertEqual('Expenses cannot be negative', str(context.exception))

    def test_room_calculate_expenses_without_children(self):
        result = self.room.calculate_expenses()
        self.assertEqual(0, result)

    def test_room__calculate_expense_with_children(self):
        result = self.room.calculate_expenses([Child(20, 1, 3, 4), Child(10, 1, 3, 4)])
        self.assertEqual(1380, result)
