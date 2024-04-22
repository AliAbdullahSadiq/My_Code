class Character:
    def __init__(self, name, x, y):
        self.__Name = name      # private string
        self.__XPosition = x    # private integer
        self.__YPosition = y    # private integer
        
    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self, valx):
        self.__XPosition += valx  
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        if self.__XPosition < 0 :
            self.__XPosition = 0    
        
    def SetYPosition(self, valy):
        self.__YPosition += valy  
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        if self.__YPosition < 0 :
            self.__YPosition = 0
    
    def Move(self, dir): 
        if dir == "up":
            self.SetYPosition(10)
        elif dir == "down":
            self.SetYPosition(-10)
        elif dir == "left":
            self.SetXPosition(-10)
        elif dir == "right":
            self.SetXPosition(10)
            
Jack = Character("Jack", 50, 50)            

class BikeCharacter(Character):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        
    def Move(self, dir):
        if dir == "up":
            super().SetYPosition(20)
        elif dir == "down":
            super().SetYPosition(-20)
        elif dir == "left":
            super().SetXPosition(-20)
        elif dir == "right":
            super().SetXPosition(20)

Karla = BikeCharacter("Karla", 100, 50) 

charactername = input("Would you like to move Jack or Karla? ").lower()
while charactername != "jack" and charactername != "karla":
    charactername = input("Invalid input, enter again: ").lower()
    
direction = input("Please enter the direction you would like the character to move: ")     
while direction not in ["up", "down", "left", "right"]:
    direction = input("Invalid input, enter again: ") 

if charactername == "jack":
    Jack.Move(direction)
    print("Jack's new position is, X=", Jack.GetXPosition(), "Y=", Jack.GetYPosition())
else:
    Karla.Move(direction)
    print("Karla's new position is, X=", Karla.GetXPosition(), "Y=", Karla.GetYPosition())    
