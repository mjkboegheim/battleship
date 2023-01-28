import random

# A MINIMUM OF TWO SHIPS ARE REQUIRED!

ships = (
    ["Carrier", 5],
    ["Battleship", 4],
    ["Destroyer", 3],
    ["Submarine", 3],
    ["Patrol Boat", 2]
)


class Ship:
    # --- CONSTRUCTOR ---#

    def __init__(self, name, length, destroyed=False):
        self.name = name
        self.length = length
        self.hit_points = length
        self.destroyed = destroyed
        self.position = []

    @staticmethod
    def positionShip(ship, game):
        possible_position = []
        rand = random.random()

        if rand > 0.499999999999:
            direction = "vertical"
            increment = 1
        else:
            direction = "horizontal"
            increment = 10

        rand_letter = random.choice(game.letters)
        rand_number = random.choice(game.numbers)
        position = rand_letter + rand_number

        index = game.indexes.index(position)
        start_index = index

        horizontal_calc = index + ((ship.length - 1) * increment)

        if direction == "vertical":
            if index >= 10 > int(str(index)[1:]) + ((ship.length - 1) * increment):
                ship.determinePosition(increment, ship, ship.length, possible_position, start_index, game)
            elif index < 10 and index + (ship.length - 1) < 10:
                ship.determinePosition(increment, ship, ship.length, possible_position, start_index, game)
            else:
                ship.positionShip(ship, game)

        elif direction == "horizontal":
            if horizontal_calc < 100:
                ship.determinePosition(increment, ship, ship.length, possible_position, start_index, game)
            elif index < 10 and horizontal_calc < 10:
                ship.determinePosition(increment, ship, ship.length, possible_position, start_index, game)
            else:
                ship.positionShip(ship, game)

    @staticmethod
    def determinePosition(increment, ship, ship_length, possible_position, start_index, game):
        if len(possible_position) is ship_length:
            Ship.placeShipOnBoard(possible_position, ship, game)
            print(possible_position)
        else:
            if not game.fields[start_index].filled:
                possible_position.append(start_index)
                if len(possible_position) != ship_length:
                    start_index += increment
                    ship.determinePosition(increment, ship, ship_length, possible_position, start_index, game)
                else:
                    ship.determinePosition(increment, ship, ship_length, possible_position, start_index, game)
            else:
                ship.positionShip(ship, game)

    @staticmethod
    def placeShipOnBoard(position, ship, game):
        [ship.fillUpField(spot, ship, game) for spot in position]

    @staticmethod
    def fillUpField(spot, ship, game):
        game.fields[spot].filled = True
        game.fields[spot].shipName = ship.name
