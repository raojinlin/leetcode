import unittest
from lettcode.DesignParkingSystem import ParkingSystem


class ParkingSystemTest(unittest.TestCase):
    def test_parking_system(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertTrue(parking_system.addCar(1))
        self.assertTrue(parking_system.addCar(2))
        self.assertFalse(parking_system.addCar(3))
        self.assertFalse(parking_system.addCar(1))
        self.assertFalse(parking_system.addCar(2))
