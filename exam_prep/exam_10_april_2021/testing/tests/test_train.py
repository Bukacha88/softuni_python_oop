from unittest import TestCase

from exam_prep.exam_10_april_2021.testing.project.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('test name', 2)

    def test_train__init__(self):
        self.assertEqual('test name', self.train.name)
        self.assertEqual(50, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_train_add_when_train_full(self):
        self.train.add('Jack')
        self.train.add('John')
        with self.assertRaises(ValueError) as context:
            self.train.add('Jim')
        self.assertEqual("Train is full", str(context.exception))

    def test_train_add_when_passenger_in_passengers(self):
        self.train.add('Jack')
        with self.assertRaises(ValueError) as context:
            self.train.add('Jack')
        self.assertEqual("Passenger Jack Exists", str(context.exception))

    def test_train_add_when_successful(self):
        result = self.train.add('Jack')
        self.assertEqual("Added passenger Jack", result)

    def test_train_remove_when_passenger_not_in_passengers(self):
        self.train.add('Jack')
        with self.assertRaises(ValueError) as context:
            self.train.remove('John')
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_train_remove_when_successful(self):
        self.train.add('Jack')
        result = self.train.remove('Jack')
        self.assertEqual("Removed Jack", result)


