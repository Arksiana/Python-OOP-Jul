from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_attr_are_sett(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_expect_fuel_decrease(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_drive_not_enough_fuel_expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_with_enough_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)
        self.vehicle.refuel(1)
        self.assertEqual(44.75, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        result = self.vehicle.__str__()
        actual = f"The vehicle has 200 " \
               f"horse power with 50 fuel left and 1.25 fuel consumption"

        self.assertEqual(actual, result)
if __name__ == '__main__':
    main()