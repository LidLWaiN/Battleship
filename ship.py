class Ship:
    def __init__(self, length):
        self.length = length
        self.positions = []  # Lista med tuples (t.ex. [(2,2), (2,3)])
        self.hits = set()

    def place(self, start_coord, direction):
        row, col = start_coord
        self.positions = []

        if direction.upper() == "H":
            for i in range(self.length):
                self.positions.append((row, col + i))
        elif direction.upper() == "V":
            for i in range(self.length):
                self.positions.append((row + i, col))
        else:
            raise ValueError("Riktning måste vara 'H' eller 'V'.")

    def register_hit(self, coord):
        if coord in self.positions:
            self.hits.add(coord)
            return True
        return False

    def is_sunk(self):
        return set(self.positions) == self.hits
