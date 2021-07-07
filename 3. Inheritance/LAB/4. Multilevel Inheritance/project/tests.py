import unittest

from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle


class Tests(unittest.TestCase):
    def test_vehicle(self):
        v = Vehicle()
        self.assertEqual(v.move(), "moving...")

    def test_car(self):
        c = Car()
        self.assertEqual(c.drive(), "driving...")
        self.assertEqual(c.__class__.__bases__[0].__name__, "Vehicle")

    def test_sports_car(self):
        s = SportsCar()
        self.assertEqual(s.race(), "racing...")
        self.assertEqual(s.__class__.__bases__[0].__name__, "Car")


if __name__ == "__main__":
    unittest.main()