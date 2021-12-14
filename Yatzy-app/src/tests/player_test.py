import unittest
import pytest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Tester")

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def reset_counter(driver):
        driver.counter = 0

    def test_print_score(self):

        self.player.print_score()
        captured = self.capsys.readouterr()
        self.assertEqual(
            ("Tester's current total score is: 0\n\n"), captured.out)

    def test_add_score(self):
        with self.capsys.disabled():
            self.player.add_score(5, "aces")
        self.player.print_score()
        captured = self.capsys.readouterr()

        self.assertEqual(
            "Tester's current total score is: 5\n\n", captured.out)

    def test_check_for_bonus(self):
        with self.capsys.disabled():
            self.player.add_score(70, "aces")
            self.player.check_for_bonus()

        self.player.print_score()
        captured = self.capsys.readouterr()
        self.assertEqual(
            "Tester's current total score is: 120\n\n", captured.out)
