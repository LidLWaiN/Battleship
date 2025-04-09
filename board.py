class Board:
    def __init__(self, size=10):
        self.size = size
        self.ships = []
        self.shots_taken = set()

    def place_ship(self, ship):
        # Kontrollera att inga positioner krockar med redan placerade skepp
        for existing_ship in self.ships:
            if any(pos in existing_ship.positions for pos in ship.positions):
                return False
        self.ships.append(ship)
        return True

    def receive_shot(self, coord):
        if coord in self.shots_taken:
            return "Already shot"
        self.shots_taken.add(coord)
        for ship in self.ships:
            if ship.register_hit(coord):
                return "Hit"
        return "Miss"

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def display_public(self):
        print("  " + " ".join(str(i + 1) for i in range(self.size)))
        for row in range(self.size):
            row_display = []
            for col in range(self.size):
                coord = (row, col)
                if coord in self.shots_taken:
                    if any(coord in ship.positions and coord in ship.hits for ship in self.ships):
                        row_display.append("X")
                    else:
                        row_display.append("O")
                else:
                    row_display.append("~")
            print(f"{row + 1:2} " + " ".join(row_display))
