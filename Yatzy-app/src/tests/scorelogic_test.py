import unittest
from scorelogic import Categories


class TestScoring(unittest.TestCase):
    def setUp(self):
        self.dice = [1, 2, 3, 4, 5]
        self.paired_dice = [1, 2, 3, 2, 1]
        self.scores = Categories()

    def test_check_aces(self):
        score = self.scores.check_aces(self.dice)
        self.assertEqual(1, score)

    def test_check_two_pairs(self):
        score = self.scores.check_two_pairs(self.paired_dice)
        self.assertEqual(6, score)
