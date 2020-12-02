import unittest
from unittest.mock import *
from src.Checker import Checker


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.temp = Checker()

    def test_before_17_not_played(self):
        self.temp.laptop.getTime = Mock(name='getTime')
        self.temp.laptop.getTime.return_value = 15
        self.temp.laptop.wavWasPlayed = Mock(name='wavWasPlayed')
        self.temp.laptop.wavWasPlayed.return_value = False
        result = self.temp.reset("song.mp3")
        self.assertEqual(result, False)

    def test_after_17_played(self):
        self.temp.laptop.getTime = Mock(name='getTime')
        self.temp.laptop.getTime.return_value = 18
        self.temp.laptop.wavWasPlayed = Mock(name='wavWasPlayed')
        self.temp.laptop.wavWasPlayed.return_value = True
        result = self.temp.reset("song.mp3")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()