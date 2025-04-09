class GameEngine:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_index = 0

    def current_player(self):
        return self.players[self.current_index]

    def opponent(self):
        return self.players[1 - self.current_index]

    def take_turn(self, coord):
        result = self.opponent().board.receive_shot(coord)

        # Kolla om motståndaren förlorat
        if self.opponent().board.all_ships_sunk():
            return f"{self.current_player().name} wins!"

        # Byt tur
        self.current_index = 1 - self.current_index
        return result
