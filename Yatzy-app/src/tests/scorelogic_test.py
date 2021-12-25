import unittest
from scorelogic import Categories


class TestScoring(unittest.TestCase):
    def setUp(self):
        self.dice = [1, 2, 3, 4, 5]
        self.high_straight = [2, 3, 4, 5, 6]
        self.paired_dice = [1, 2, 3, 2, 1]
        self.full_house = [1, 2, 2, 2, 1]
        self.yatzy = [5, 5, 5, 5, 5]
        self.scores = Categories()

    def test_check_singles(self):
        score = self.scores.check_aces(self.dice)
        self.assertEqual(1, score)
        score = self.scores.check_twos(self.dice)
        self.assertEqual(2, score)
        score = self.scores.check_threes(self.dice)
        self.assertEqual(3, score)
        score = self.scores.check_fours(self.dice)
        self.assertEqual(4, score)
        score = self.scores.check_fives(self.dice)
        self.assertEqual(5, score)
        score = self.scores.check_sixes(self.dice)
        self.assertEqual(0, score)

    def test_check_one_pair(self):

        score = self.scores.check_one_pair(self.paired_dice)
        self.assertEqual(4, score)

    def test_check_two_pairs(self):

        score = self.scores.check_two_pairs(self.paired_dice)
        self.assertEqual(6, score)

    def test_check_three_of_a_kind(self):
        score = self.scores.check_three_of_a_kind(self.yatzy)
        self.assertEqual(15, score)

    def test_check_four_of_a_kind(self):
        score = self.scores.check_four_of_a_kind(self.yatzy)
        self.assertEqual(20, score)

    def test_check_full_house(self):
        score = self.scores.check_full_house(self.full_house)
        self.assertEqual(8, score)

    def test_check_low_straight(self):
        score = self.scores.check_low_straight(self.dice)
        self.assertEqual(15, score)

    def test_check_high_straight(self):
        score = self.scores.check_high_straight(self.high_straight)
        self.assertEqual(20, score)

    def test_check_yatzy(self):
        score = self.scores.check_yatzy(self.yatzy)
        self.assertEqual(50, score)
