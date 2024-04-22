class Balloon:
    def __init__(self, Health, Colour, DefenseItem):
        self._health = Health
        self._colour = Colour
        self._defense_item = DefenseItem

    def Constructor(self, Colour, DefenseItem):
        self._health = 100
        self._colour = ''
        self._defense_item = ''

    def ChangeHealth(self, Change):
        Health = Health + Change
    
    def GetDefenceItem(self):
        return self.DefenseItem
    
    def CheckHealth(self):
        if self.Health < 0:
            return True
        else:
            return False
        
#main
UserColor = input("Enter the color: ")
UserDefenseItem = input("Enter the defense item: ")
Baloon1 = Balloon(0, UserColor, UserDefenseItem)

def Defend(Balloon):
    OpponentStrength = int(input("Opponent Strength: "))