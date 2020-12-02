import unittest
from unittest.mock import *
from src.Car import *


class TestCar(unittest.TestCase):
    def setUp(self):
        self.temp = Car()

    def test_needsFuel_return_true(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = True
        self.assertEqual(self.temp.needsFuel(), True)

    def test_needsFuel_return_false(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = False
        self.assertEqual(self.temp.needsFuel(), False)

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature_patch(self, mock_method):
        mock_method.return_value = 80
        result = self.temp.getEngineTemperature()
        self.assertEqual(result, 80)

    @patch.object(Car, 'driveTo')
    def test_driveTo_patch(self, mock_method):
        mock_method.return_value = "Las Vegas"
        result = self.temp.driveTo("Las Vegas")
        self.assertEqual(result, "Las Vegas")


if __name__ == '__main__':
    unittest.main()