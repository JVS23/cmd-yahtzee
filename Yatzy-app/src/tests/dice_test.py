import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        self.dice.roll()
        self.assertEqual(5, len(self.dice.print()))

    def test_dicelist_reset(self):

        self.dice.roll()
        self.dice.dicelist_reset()
        self.assertEqual(0, len(self.dice.print()))
