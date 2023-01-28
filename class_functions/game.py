from class_functions.ship import Ship


class Game:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

    indexes = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
               "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
               "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
               "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10",
               "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10",
               "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
               "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
               "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10",
               "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10",
               "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10",)

    # --- CONSTRUCTOR ---")
    def __init__(self, name, gameStarted=True, gameFinished=False):
        self.name = name
        self.gameStarted = gameStarted
        self.gameFinished = gameFinished
        self.fields = []

    # --- BOARD --- #

    def createBoard(self):
        # creates a field range from 0 to 99 (A1 to J10)
        fieldRange = range(100)
        for field in fieldRange:
            self.fields.append(Field(field, self.indexes[field]))

    # printing the game board
    def printBoard(self):
        print(
            "  " + "|" + "A" + "|" + "B" + "|" + "C" + "|" + "D" + "|" + "E" + "|" + "F" + "|" + "G" + "|" + "H" + "|" + "I" + "|" + "J")
        print(
            "1 " + "|" + self.fields[0].content + "|" + self.fields[10].content + "|" + self.fields[20].content + "|" +
            self.fields[30].content + "|" + self.fields[40].content + "|" + self.fields[50].content + "|" + self.fields[
                60].content + "|" + self.fields[70].content + "|" + self.fields[80].content + "|" + self.fields[
                90].content)
        print(
            "2 " + "|" + self.fields[1].content + "|" + self.fields[11].content + "|" + self.fields[21].content + "|" +
            self.fields[31].content + "|" + self.fields[41].content + "|" + self.fields[51].content + "|" + self.fields[
                61].content + "|" + self.fields[71].content + "|" + self.fields[81].content + "|" + self.fields[
                91].content)
        print(
            "3 " + "|" + self.fields[2].content + "|" + self.fields[12].content + "|" + self.fields[22].content + "|" +
            self.fields[32].content + "|" + self.fields[42].content + "|" + self.fields[52].content + "|" + self.fields[
                62].content + "|" + self.fields[72].content + "|" + self.fields[82].content + "|" + self.fields[
                92].content)
        print(
            "4 " + "|" + self.fields[3].content + "|" + self.fields[13].content + "|" + self.fields[23].content + "|" +
            self.fields[33].content + "|" + self.fields[43].content + "|" + self.fields[53].content + "|" + self.fields[
                63].content + "|" + self.fields[73].content + "|" + self.fields[83].content + "|" + self.fields[
                93].content)
        print(
            "5 " + "|" + self.fields[4].content + "|" + self.fields[14].content + "|" + self.fields[24].content + "|" +
            self.fields[34].content + "|" + self.fields[44].content + "|" + self.fields[54].content + "|" + self.fields[
                64].content + "|" + self.fields[74].content + "|" + self.fields[84].content + "|" + self.fields[
                94].content)
        print(
            "6 " + "|" + self.fields[5].content + "|" + self.fields[15].content + "|" + self.fields[25].content + "|" +
            self.fields[35].content + "|" + self.fields[45].content + "|" + self.fields[55].content + "|" + self.fields[
                65].content + "|" + self.fields[75].content + "|" + self.fields[85].content + "|" + self.fields[
                95].content)
        print(
            "7 " + "|" + self.fields[6].content + "|" + self.fields[16].content + "|" + self.fields[26].content + "|" +
            self.fields[36].content + "|" + self.fields[46].content + "|" + self.fields[56].content + "|" + self.fields[
                66].content + "|" + self.fields[76].content + "|" + self.fields[86].content + "|" + self.fields[
                96].content)
        print(
            "8 " + "|" + self.fields[7].content + "|" + self.fields[17].content + "|" + self.fields[27].content + "|" +
            self.fields[37].content + "|" + self.fields[47].content + "|" + self.fields[57].content + "|" + self.fields[
                67].content + "|" + self.fields[77].content + "|" + self.fields[87].content + "|" + self.fields[
                97].content)
        print(
            "9 " + "|" + self.fields[8].content + "|" + self.fields[18].content + "|" + self.fields[28].content + "|" +
            self.fields[38].content + "|" + self.fields[48].content + "|" + self.fields[58].content + "|" + self.fields[
                68].content + "|" + self.fields[78].content + "|" + self.fields[88].content + "|" + self.fields[
                98].content)
        print(
            "10" + "|" + self.fields[9].content + "|" + self.fields[19].content + "|" + self.fields[29].content + "|" +
            self.fields[39].content + "|" + self.fields[49].content + "|" + self.fields[59].content + "|" + self.fields[
                69].content + "|" + self.fields[79].content + "|" + self.fields[89].content + "|" + self.fields[
                99].content)

    # --- SHIPS -------------------------------------------------------------------------------------------------------------------------------------------------- #

    @staticmethod
    def createShip(x):
        # x[0]: name, x[1]: length
        return Ship(x[0], x[1])

    @staticmethod
    def placeShipsOnBoard(ships, game):
        [x.positionShip(x, game) for x in ships]

    # --- GAME -------------------------------------------------------------------------------------------------------------------------------------------------- #

    @staticmethod
    def checkCoordinate(selected_field, game):
        for field in game.fields:
            if field.fieldNumber == selected_field:
                return field

    @staticmethod
    def gameOverCheck(ships, game):
        count = 0

        for ship in ships:
            if ship.hit_points == 0:
                count += 1
            else:
                continue

        if count == len(ships):
            game.gameFinished = True


class Field:
    def __init__(self, index, fieldNumber):
        self.index = index
        self.fieldNumber = fieldNumber
        self.content = "-"
        self.hit = False
        self.filled = False
        self.shipName = ""

    # setter method
    def set_field(self):
        self.hit = True
