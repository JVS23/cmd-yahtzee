import unittest
import dice


class TestRollDice(unittest.TestCase):
    def test_roll(self):
        list_of_five = dice.roll()
        self.assertEqual(5, len(list_of_five))
