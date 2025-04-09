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

    def test_receive_shot_sinks_ship(self):
        board = Board(size=5)
        ship = Ship(length=1)
        ship.place((2, 2), "H")
        board.place_ship(ship)
        result = board.receive_shot((2, 2))
        self.assertEqual(result, "Hit and sunk")


    def test_all_ships_sunk(self):
        board = Board(size=5)
        ship = Ship(length=1)
        ship.place((4, 4), "H")
        board.place_ship(ship)
        board.receive_shot((4, 4))
        self.assertTrue(board.all_ships_sunk())

    def test_all_ships_sunk_when_no_ships(self):
        board = Board(size=5)
        self.assertTrue(board.all_ships_sunk())

    def test_place_ship_out_of_bounds_horizontal(self):
        board = Board(size=5)
        ship = Ship(length=3)
        ship.place((0, 4), "H")  # Plats 0,4 – 0,5 – 0,6 => utanför
        result = board.place_ship(ship)
        self.assertFalse(result)

    def test_place_ship_out_of_bounds_vertical(self):
        board = Board(size=5)
        ship = Ship(length=4)
        ship.place((3, 1), "V")  # Plats 3,1 – 4,1 – 5,1 – 6,1 => utanför
        result = board.place_ship(ship)
        self.assertFalse(result)

    def test_place_ship_negative_coordinates(self):
        board = Board(size=5)
        ship = Ship(length=2)
        ship.place((-1, 0), "H")  # Negativ rad
        result = board.place_ship(ship)
        self.assertFalse(result)

    def test_display_public_runs_without_error(self):
        board = Board(size=5)
        ship = Ship(length=2)
        ship.place((1, 1), "H")
        board.place_ship(ship)
        board.receive_shot((1, 1))  # träff
        board.receive_shot((0, 0))  # miss

        try:
            board.display_public()  # bara för att täcka raderna
        except Exception as e:
            self.fail(f"display_public() kastade undantag: {e}")

if __name__ == '__main__':
    unittest.main()
