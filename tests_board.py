import unittest
from board import Board
from ship import Ship

class TestBoard(unittest.TestCase):

    def test_place_ship_successfully(self):
        board = Board(size=5)
        ship = Ship(length=3)
        ship.place((1, 1), "H")
        success = board.place_ship(ship)
        self.assertTrue(success)
        self.assertIn(ship, board.ships)

    def test_prevent_overlapping_ships(self):
        board = Board(size=5)
        ship1 = Ship(length=3)
        ship1.place((0, 0), "H")
        ship2 = Ship(length=2)
        ship2.place((0, 1), "V")  # Överlappar (0,1)
        board.place_ship(ship1)
        success = board.place_ship(ship2)
        self.assertFalse(success)

    def test_receive_shot_hit(self):
        board = Board(size=5)
        ship = Ship(length=2)
        ship.place((2, 2), "H")
        board.place_ship(ship)
        result = board.receive_shot((2, 2))
        self.assertEqual(result, "Hit")

    def test_receive_shot_miss(self):
        board = Board(size=5)
        ship = Ship(length=2)
        ship.place((2, 2), "H")
        board.place_ship(ship)
        result = board.receive_shot((0, 0))
        self.assertEqual(result, "Miss")

    def test_receive_shot_repeat(self):
        board = Board(size=5)
        ship = Ship(length=1)
        ship.place((1, 1), "H")
        board.place_ship(ship)
        board.receive_shot((1, 1))  # första skott
        result = board.receive_shot((1, 1))  # andra skott på samma plats
        self.assertEqual(result, "Already shot")

    def test_all_ships_sunk(self):
        board = Board(size=5)
        ship = Ship(length=1)
        ship.place((4, 4), "H")
        board.place_ship(ship)
        board.receive_shot((4, 4))
        self.assertTrue(board.all_ships_sunk())

if __name__ == '__main__':
    unittest.main()
