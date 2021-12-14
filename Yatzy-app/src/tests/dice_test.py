import unittest
from unittest.mock import patch
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def get_input(text):
        return input(text)

    def test_roll(self):
        self.dice.roll()
        self.assertEqual(5, len(self.dice.print()))

    def test_dice_list_reset(self):

        self.dice.roll()
        self.dice.dice_list_reset()
        self.assertEqual(0, len(self.dice.print()))

    @patch('builtins.input', return_value='1')
    def test_dice_list_choose(self, mock_input):

        self.dice_list = [1, 2, 3, 4, 5]

        new_dice = self.dice.choose()
        self.assertNotEqual([1, 2, 3, 4, 5], self.dice.print())
