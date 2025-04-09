import unittest
from player import Player
from board import Board

class TestPlayer(unittest.TestCase):

    def test_player_has_name(self):
        player = Player("Jesper")
        self.assertEqual(player.name, "Jesper")

    def test_player_has_board(self):
        player = Player("Jesper")
        self.assertIsInstance(player.board, Board)

    def test_player_can_receive_shot(self):
        player = Player("Jesper")
        result = player.board.receive_shot((0, 0))  # Tomt bräde
        self.assertEqual(result, "Miss")

if __name__ == '__main__':
    unittest.main()
