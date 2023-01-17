class Game:

    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

    # --- CONSTRUCTOR ---")
    def __init__(self, name, gameStarted=True, gameFinished=False):  

        self.name = name
        self.gameStarted = gameStarted
        self.gameFinished = gameFinished
        self.fields = []

    def createBoard(self):
        #fields

        #field indexes
        indexes = ("A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1",
                 "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2",
                 "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3",
                 "A4", "D4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4",
                 "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5",
                 "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6",
                 "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7",
                 "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8",
                 "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9",
                 "A10", "B10", "C10", "D10", "E10", "G10", "H10", "I10", "I10", "J10")

        #creates a field range from 0 to 99 (A1 to J10)
        fieldRange = range(100)
        for field in fieldRange:
            self.fields.append(Field(field, indexes[field]))

    # printing the game board
    def printBoard(self, fields): 
        print("  " + "|" + "A" + "|" + "B" + "|" + "C" +  "|" + "D" +  "|" + "E" + "|" + "F" + "|" + "G" + "|" + "H" + "|" + "I" + "|" + "J")
        print("1 " + "|" +  self.fields[0].content  + "|" +  self.fields[10].content  + "|" +  self.fields[20].content  + "|" +  self.fields[30].content  + "|" +  self.fields[40].content  + "|" +  self.fields[50].content  + "|" +  self.fields[60].content  + "|" +  self.fields[70].content  + "|" +  self.fields[80].content  + "|" + self.fields[90].content)
        print("2 " + "|" +  self.fields[1].content  + "|" +  self.fields[11].content  + "|" +  self.fields[21].content  + "|" +  self.fields[31].content  + "|" +  self.fields[41].content  + "|" +  self.fields[51].content  + "|" +  self.fields[61].content  + "|" +  self.fields[71].content  + "|" +  self.fields[81].content  + "|" + self.fields[91].content )
        print("3 " + "|" +  self.fields[2].content  + "|" +  self.fields[12].content  + "|" +  self.fields[22].content  + "|" +  self.fields[32].content  + "|" +  self.fields[42].content  + "|" +  self.fields[52].content  + "|" +  self.fields[62].content  + "|" +  self.fields[72].content  + "|" +  self.fields[82].content  + "|" + self.fields[92].content )
        print("4 " + "|" +  self.fields[3].content  + "|" +  self.fields[13].content  + "|" +  self.fields[23].content  + "|" +  self.fields[33].content  + "|" +  self.fields[43].content  + "|" +  self.fields[53].content  + "|" +  self.fields[63].content  + "|" +  self.fields[73].content  + "|" +  self.fields[83].content  + "|" + self.fields[93].content )
        print("5 " + "|" +  self.fields[4].content  + "|" +  self.fields[14].content  + "|" +  self.fields[24].content  + "|" +  self.fields[34].content  + "|" +  self.fields[44].content  + "|" +  self.fields[54].content  + "|" +  self.fields[64].content  + "|" +  self.fields[74].content  + "|" +  self.fields[84].content  + "|" + self.fields[94].content )
        print("6 " + "|" +  self.fields[5].content  + "|" +  self.fields[15].content  + "|" +  self.fields[25].content  + "|" +  self.fields[35].content  + "|" +  self.fields[45].content  + "|" +  self.fields[55].content  + "|" +  self.fields[65].content  + "|" +  self.fields[75].content  + "|" +  self.fields[85].content  + "|" + self.fields[95].content )
        print("7 " + "|" +  self.fields[6].content  + "|" +  self.fields[16].content  + "|" +  self.fields[26].content  + "|" +  self.fields[36].content  + "|" +  self.fields[46].content  + "|" +  self.fields[56].content  + "|" +  self.fields[66].content  + "|" +  self.fields[76].content  + "|" +  self.fields[86].content  + "|" + self.fields[96].content )
        print("8 " + "|" +  self.fields[7].content  + "|" +  self.fields[17].content  + "|" +  self.fields[27].content  + "|" +  self.fields[37].content  + "|" +  self.fields[47].content  + "|" +  self.fields[57].content  + "|" +  self.fields[67].content  + "|" +  self.fields[77].content  + "|" +  self.fields[87].content  + "|" + self.fields[97].content )
        print("9 " + "|" +  self.fields[8].content  + "|" +  self.fields[18].content  + "|" +  self.fields[28].content  + "|" +  self.fields[38].content  + "|" +  self.fields[48].content  + "|" +  self.fields[58].content  + "|" +  self.fields[68].content  + "|" +  self.fields[78].content  + "|" +  self.fields[88].content  + "|" + self.fields[98].content )
        print("10" + "|" +  self.fields[9].content  + "|" +  self.fields[19].content  + "|" +  self.fields[29].content  + "|" +  self.fields[39].content  + "|" +  self.fields[49].content  + "|" +  self.fields[59].content  + "|" +  self.fields[69].content  + "|" +  self.fields[79].content  + "|" +  self.fields[89].content  + "|" + self.fields[99].content )

class Field:
    def __init__(self, index, fieldNumber):
        self.index = index
        self.fieldNumber = fieldNumber
        self.content = "-"
        self.hit = False
        self.filled = False
        self.shipName = ""
