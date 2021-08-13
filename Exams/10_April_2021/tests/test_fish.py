from unittest import TestCase, main

import self as self

from project.fish.freshwater_fish import FreshwaterFish


class SaltWaterFish(object):
    pass


class TestFish(TestCase):
    def setUp(self) -> None:
        self.fresh_water = FreshwaterFish('FW', 'FW', 1)
        self.salt_water_fish = SaltWaterFish('SW', 'SW', 1)

    def test_attr_are_sett(self):
        self.assertEqual(('FW', 'FW', 1), self.fresh_water.name, s)

if __name__ == '__main__':
    main()