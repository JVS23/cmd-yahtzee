import unittest
import pytest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Tester")

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_print_score(self):

        self.player.print_score()
        captured = self.capsys.readouterr()
        self.assertEqual(
            ("Tester 's current total score is:  0 \n\n"), captured.out)
