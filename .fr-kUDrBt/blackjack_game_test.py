import unittest
from blackjack_game import BlackjackGame


class TestBlackjackGame(unittest.TestCase):

    def setUp(self):
        self.blackjack_game = BlackjackGame()

    def test_something(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()