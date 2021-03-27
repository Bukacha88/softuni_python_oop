
from testing_lab.CarManager.car_manager.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    make = 'BMW'
    model = '3'
    fuel_consumption = 10
    fuel_capacity = 9
    fuel_amount = 0

    def setUp(self):
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.car.fuel_amount = 0

    def test_car__init__when_correct_attributes__expect_to_initialized(self):
        self.assertEqual(self.make, self.car.make)
        self.assertEqual(self.model, self.car.model)
        self.assertEqual(self.fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(self.fuel_capacity, self.car.fuel_capacity)
        self.assertEqual(self.fuel_amount, self.car.fuel_amount)

    def test_car_make_setter__when_None__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_model_setter__when_None__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_fuel_consumption_setter__when_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_consumption_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity_setter__when_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_amount_setter__when_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_car_refuel__when_fuel_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            fuel = 0
            self.car.refuel(fuel)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_fuel_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            fuel = -3
            self.car.refuel(fuel)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_fuel_positive__expect_fuel_amount_to_increase(self):
        fuel = 10
        self.car.refuel(fuel)
        self.assertEqual(10, self.car.fuel_amount)

    # def test_car_refuel__when__fuel_amount_greater_than_fuel_capacity__expect_fuel_amount_to_be_set_as_fuel_capacity(self):
    #     self.car.refuel(10)
    #     self.fuel_amount = self.fuel_capacity
    #     self.assertEqual(9, self.car.fuel_amount)

    def test_car_refuel__when__fuel_amount_greater_than_fuel_capacity__expect_fuel_amount_to_be_fuel_capacity(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_drive__when_needed_is_greater_than_fuel_amount__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(150)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_car_drive__when_needed_is_equal_than_fuel_amount__expect_exception(self):
        self.car.fuel_amount = 100
        self.car.drive(100)
        self.assertEqual(90, self.car.fuel_amount)

    def test_fuel_amount_after_driver(self):
        self.car.refuel(5)
        self.car.drive(5)
        self.assertEqual(4.5, self.car.fuel_amount)


if __name__ == '__main__':
    main()
