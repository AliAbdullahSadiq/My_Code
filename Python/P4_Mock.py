# Question 1
import random
Player = [0]*9
NumbersColours = []

for i in range(0,9):
    Player[i] = random.randint(1,5)

try:
    MyFile = open(r"C:\Users\Student-PC7\Desktop\Ali Abdullah Sadiq batch 2\computer science P4 MOCK 2024\Favourite.txt",'r')
    data = MyFile.readline.strip
    NumbersColours[0][0] = data
    while data != "":
        for i in range(0,9):
            data = MyFile.readline.strip
            NumbersColours[1][i] = data
            data = MyFile.readline.strip
            NumbersColours[0][i]
    MyFile.close
except IOError:
    print("File does not exist")

def Sort():
    NumbersColours[0].sort

Sort()


print(Player)
print(NumbersColours)


def RecursivePoints(count):
    Total = count^2
    RecursivePoints(count - 1)

# Question 2
class ListElement():
    def __init__(self, c, p):
        self.Country = c
        self.Pointer = p



#Declare array CountryList of type ListElement
#Declare ListNode of type integer
#Declare LastNode of type integer

CountryList = [ListElement("",0)]*8
ListHead = 0
LastNode = 0

CountryList[0] = ListElement("Wales",1)
CountryList[1] = ListElement("Scotland",2)
CountryList[2] = ListElement("Brazil",4)
CountryList[3] = ListElement("",-1)
CountryList[4] = ListElement("Canada",5)
CountryList[5] = ListElement("",6)
CountryList[6] = ListElement("",7)
CountryList[7] = ListElement("",3)

ListHead = 0
LastNode = 3

def OutputNodes():
    for i in range(0,8):
        print(i)
        ptr = CountryList[i].Country
        print(ptr)
        con = CountryList[i].Pointer
        print(con)
        print(" ")

OutputNodes()

def DeleteNode(NodeValue, ThisPointer, PreviousPtr):
    if CountryList[ThisPointer].Country == NodeValue:
        CountryList[ThisPointer].Country = ""
        if ListHead == ThisPointer:
            ListHead = LastNode
        else:
            CountryList[PreviousPtr].Pointer = CountryList[ThisPointer].Pointer
        #Endif
        CountryList[LastNode].Pointer = LastNode - 1
        LastNode = ThisPointer
    else:
        if CountryList[ThisPointer].Pointer != -1:
            DeleteNode(NodeValue, ThisPointer - 1, ThisPointer)
        else:
            print("DOES NOT EXIST")
        #EndIf
    #EndIf
#EndProcedure
            
DeleteNode("Scotland", 0, -1)
OutputNodes()

# Question 3
from datetime import datetime

class Character:
    def __init__(self, name, date, intel, speed):
        #Declare CharacterName as string
        #Declare DateOfBirth as date
        #Declare Intelligence as real
        #Declare Speed as integer

        self.CharacterName = name
        self.DateOfBirth = date
        self.Intelligence = intel
        self.Speed = speed

    def GetIntelligence(self, intel):
        return self.Intelligence
    
    def GetName(self, name):
        return self.CharacterName
    
    def SetIntelligence(self, intel):
        self.Intelligence = intel

    def Learn(self):
        self.Intelligence += (self.Intelligence)/10

    def ReturnAge(self):
        YearNow = 2023
        YearChar = map(int, self.DateOfBirth.split('-'))
        return YearNow - YearChar

class MagicCharacter(Character):
    #Declare Element as string

    #def __init__(self, element):
        #self.super(Character, Element) = element
    
    def Learn(self, elememnt, intel):
        if self.Element == "fire" or self.Element == "water":
            self.Intelligence += (self.Intelligence)/5
        elif self.Element == "earth":
            self.Intelligence += (self.Intelligence)/(100/30)
        else:
            self.Intelligence += (self.Intelligence)/10            

FirstCharacter = Character("Royal", datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()

name = FirstCharacter.CharacterName
print(name)
DoB = FirstCharacter.DateOfBirth
print(DoB)
intel = FirstCharacter.Intelligence
print(intel)
speed = FirstCharacter.Speed
print(speed)

#FirstMagic = MagicCharacter("Light", datetime(2018, 3, 3), 75, 22, "fire")

#FirstMagic.Learn()

name = "Light"
print(name)
DoB = datetime(2018, 3, 3)
print(DoB)
intel = 75
print(intel)
speed = 22
print(speed)
element = "fire"
print(element)

# test
def RecursivePoints(count):
    Total = 0
    if count == 0:
        return Total
    else:
        Total = int(Total + (count**2))
        RecursivePoints(count-1)   

print(RecursivePoints(6))

num = 36
num += 25
num += 16
num += 9
num += 4
num += 1
print(' ')
print(num)
print(' ')

num = 4
num += 4/10
print(num)