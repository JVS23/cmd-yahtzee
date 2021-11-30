import unittest
from dice import Dice

class TestRollDice(unittest.TestCase):
    def test_roll(self):
        test_dice = Dice()
        list_of_five = test_dice.roll()
        self.assertEqual(5, len(list_of_five))
