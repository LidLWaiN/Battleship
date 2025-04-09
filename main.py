from player import Player
from ship import Ship
from game_engine import GameEngine

def place_ships(player):
    print(f"\n{player.name}, placera dina skepp:")
    for length in [2, 3]:  # Du kan lägga till fler skepp
        while True:
            try:
                print(f"Skepp med längd {length}")
                coords = input("Startposition (ex: 1 1): ")
                row, col = map(int, coords.strip().split())
                direction = input("Riktning (H/V): ").strip().upper()
                ship = Ship(length)
                ship.place((row - 1, col - 1), direction)
                if player.board.place_ship(ship):
                    break
                else:
                    print("Krock med annat skepp. Försök igen.")
            except:
                print("Felaktig input. Försök igen.")

def play_game():
    print("🛳️ Välkommen till Battleship!\n")
    p1 = Player(input("Spelare 1 namn: "))
    p2 = Player(input("Spelare 2 namn: "))

    place_ships(p1)
    place_ships(p2)

    game = GameEngine(p1, p2)

    while True:
        current = game.current_player()
        print("\nMotståndarens bräde:")
        game.opponent().board.display_public()
        print(f"\n{current.name}s tur:")
        coords = input("Ange koordinat att skjuta på (ex: 1 1): ")
        try:
            row, col = map(int, coords.strip().split())
            result = game.take_turn((row - 1, col - 1))
            print(f"👉 Resultat: {result}")
            if "wins" in result:
                print("🎉 Spelet är slut!")
                print("\nSlutställning:\n")

                print(f"{game.players[0].name}s bräde:")
                game.players[0].board.display_public()

                print(f"\n{game.players[1].name}s bräde:")
                game.players[1].board.display_public()
                break
        except:
            print("Felaktig input. Försök igen.")

if __name__ == "__main__":
    play_game()
