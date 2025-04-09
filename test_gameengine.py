import unittest
from game_engine import GameEngine
from player import Player
from ship import Ship

class TestGameEngine(unittest.TestCase):

    def setUp(self):
        self.p1 = Player("Spelare 1")
        self.p2 = Player("Spelare 2")
        self.game = GameEngine(self.p1, self.p2)

        # Placera skepp på båda spelare
        ship1 = Ship(1)
        ship1.place((0, 0), "H")
        self.p1.board.place_ship(ship1)

        ship2 = Ship(1)
        ship2.place((1, 1), "H")
        self.p2.board.place_ship(ship2)

    def test_game_starts_with_player1(self):
        self.assertEqual(self.game.current_player().name, "Spelare 1")

    def test_take_turn_hit(self):
        # Placera större skepp för att undvika direkt vinst
        self.p2.board.ships.clear()
        ship = Ship(2)
        ship.place((1, 1), "H")
        self.p2.board.place_ship(ship)

        result = self.game.take_turn((1, 1))  # träff, men inte sänkt
        self.assertEqual(result, "Hit")


    def test_switch_turns(self):
        # Se till att spelet inte avslutas efter första skottet
        self.p2.board.ships.clear()
        ship = Ship(2)
        ship.place((1, 1), "H")
        self.p2.board.place_ship(ship)

        self.game.take_turn((1, 1))
        self.assertEqual(self.game.current_player().name, "Spelare 2")


    def test_game_win_condition(self):
        result = self.game.take_turn((1, 1))
        self.assertIn("wins", result)

if __name__ == '__main__':
    unittest.main()
