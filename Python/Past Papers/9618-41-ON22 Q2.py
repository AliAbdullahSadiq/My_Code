class Card:

    # DECLARE Number of Card as an integer
    # DECLARE Number of Card as a string

    def __init__(self, Number, Colour):
        self._number = Number
        self._Colour = Colour

    def GetNumber(self):
        return self._number

    def GetColour(self):
        return self._Colour
    
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

class Hand:

    def __init__(self, Cards, FirstCard, NumberCards):
        self._cards = [] * 9
        self._firstcard = FirstCard
        self._numbercards = NumberCards

    def GetCard(self):
        return self._cards
    
    def GetFirstCard(self):
        return self._firstcard
    
    def GetNumberCards(self):
        return self._numbercards