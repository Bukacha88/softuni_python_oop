from unittest import TestCase

from exam_prep.python_oop_exam_16_aug_2020.project.hardware.hardware import Hardware
from exam_prep.python_oop_exam_16_aug_2020.project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware('SSD', 'Heavy', 200, 200)

    def test_hardware__init__expect_to_initialized(self):
        self.assertEqual('SSD', self.hardware.name)
        self.assertEqual('Heavy', self.hardware.type)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual(200, self.hardware.capacity)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_install__when_capacity_less_than_consumption(self):
        software = Software('Linux', 'Light', 250, 10)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(context.exception))

    def test_hardware_install__when_memory_less_than_consumption(self):
        software = Software('Linux', 'Light', 10, 250)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(context.exception))

    def test_hardware_install__when_enogh_memory_and_capacity(self):
        software = Software('Linux', 'Light', 10, 20)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)

    def test_hardware_uninstall__when_software_in_software_components(self):
        software = Software('Linux', 'Light', 10, 20)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)
