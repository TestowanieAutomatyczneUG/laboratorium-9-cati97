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
    

