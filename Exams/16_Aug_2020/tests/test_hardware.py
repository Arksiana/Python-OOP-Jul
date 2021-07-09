from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware('Hardware', 'Type', 100, 100)
        self.software = Software('Software', 'Type', 50, 50)

    def test_attr_are_sett(self):
        self.assertEqual('Hardware', self.hardware.name)
        self.assertEqual('Type', self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(100, self.hardware.memory)
        self.assertEqual([ ], self.hardware.software_components)

    def test_install_software_successes(self):
        self.hardware.install(self.software)
        self.assertEqual([self.software], self.hardware.software_components)

    def test_install_software_with_exception(self):
        self.software.memory_consumption = 200
        self.software.capacity_consumption = 200
        with self.assertRaises(Exception) as context:
            self.hardware.install(self.software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_uninstall_software(self):
        self.hardware.install(self.software)
        self.hardware.uninstall(self.software)
        self.assertEqual([ ], self.hardware.software_components)

    def test_property_used_memory(self):
        self.hardware.install(self.software)
        result = self.hardware.used_memory
        self.assertEqual(50, result)

    def test_property_used_capacity(self):
        self.hardware.install(self.software)
        result = self.hardware.used_memory
        self.assertEqual(50, result)

    def test_property_available_capacity(self):
        self.hardware.install(self.software)
        self.assertEqual(50, self.hardware.available_capacity)

    def test_property_used_memory(self):
        self.hardware.install(self.software)
        self.assertEqual(50, self.hardware.available_memory)





if __name__ == '__main__':
    main()