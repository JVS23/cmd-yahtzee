import unittest
from unittest.mock import patch
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        self.dice.roll()
        self.assertEqual(5, len(self.dice.dice_return()))

    def test_dice_list_reset(self):

        self.dice.roll()
        self.dice.dice_list_reset()
        self.assertEqual(0, len(self.dice.dice_return()))

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 7])
    def test_dice_list_choose(self, mock_inputs):

        self.dice.dice_list = [1, 2, 3, 4, 5]

        self.dice.choose()

        self.assertNotEqual([1, 2, 3, 4, 5], self.dice.dice_return())
