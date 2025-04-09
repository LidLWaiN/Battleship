import unittest
from ship import Ship  # Vi förutsätter att Ship-klassen kommer finnas i ship.py

class TestShip(unittest.TestCase):
    
    def test_create_ship_with_length(self):
        ship = Ship(length=3)
        self.assertEqual(ship.length, 3)
        self.assertEqual(ship.hits, set())

    def test_place_ship_horizontal(self):
        ship = Ship(length=3)
        ship.place((2, 2), "H")
        expected_positions = [(2, 2), (2, 3), (2, 4)]
        self.assertEqual(ship.positions, expected_positions)

    def test_place_ship_vertical(self):
        ship = Ship(length=2)
        ship.place((1, 1), "V")
        expected_positions = [(1, 1), (2, 1)]
        self.assertEqual(ship.positions, expected_positions)

    def test_register_hit_success(self):
        ship = Ship(length=2)
        ship.place((0, 0), "H")
        result = ship.register_hit((0, 0))
        self.assertTrue(result)
        self.assertIn((0, 0), ship.hits)

    def test_register_hit_miss(self):
        ship = Ship(length=2)
        ship.place((0, 0), "H")
        result = ship.register_hit((1, 1))
        self.assertFalse(result)
        self.assertNotIn((1, 1), ship.hits)

    def test_is_sunk(self):
        ship = Ship(length=2)
        ship.place((0, 0), "H")
        ship.register_hit((0, 0))
        self.assertFalse(ship.is_sunk())
        ship.register_hit((0, 1))
        self.assertTrue(ship.is_sunk())

if __name__ == '__main__':
    unittest.main()
