from class_functions.game import Game
from class_functions.ship import ships

if __name__ == "__main__":

    game = Game("Maarten")

    if game.gameStarted:
        game.createBoard()
        game.printBoard()

        # Create ship for each ship
        ships = [game.createShip(x) for x in ships]
        # ships: list of ships, game: game object
        game.placeShipsOnBoard(ships, game)

        while not game.gameFinished:
            print("\nFill in coordinates:")
            selected_field = input()

            coordinate = game.checkCoordinate(selected_field, game)

            if coordinate is None:
                print("\n")
                game.printBoard()

                print("\nYou gave invalid coordinates. Please try again!")
            else:
                ship_coordinate = game.fields[coordinate.index]

                if not ship_coordinate.filled and not ship_coordinate.hit:
                    game.fields[coordinate.index].hit = True
                    game.fields[coordinate.index].content = "-"

                    print("\n")
                    game.printBoard()
                    print("\nYou didn't hit anything. Please try again!")

                elif ship_coordinate.filled is True and ship_coordinate.hit is False:
                    game.fields[coordinate.index].hit = True
                    game.fields[coordinate.index].content = "*"

                    selected_ship = [ship for ship in ships if ship.name == ship_coordinate.shipName]
                    selected_ship[0].hit_points += -1

                    print("\n")
                    game.printBoard()
                    print("\nYou hit the " + ship_coordinate.shipName + "!")

                    if selected_ship[0].hit_points == 0:
                        print("\n")
                        game.printBoard()
                        print("\nYou destroyed the " + ship_coordinate.shipName + "!")

                elif ship_coordinate.hit is True:
                    print("\n")
                    game.printBoard()
                    print("\nYou already selected this coordinate!")

                game.gameOverCheck(ships, game)

        if game.gameFinished:
            print("\nAll ships are destroyed. You won the game!")
    else:
        print("\nSomething went wrong. You need to run the program again!")

# --- #
