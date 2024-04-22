# path = r"C:/Users/Student-PC3/Desktop/Favorite.txt"
import random

col = 2
row = 10

Players = [""]*10
NumbersColours = [[""]* col for i in range(row)]

for i in range(10):
    Players[i] = random.randint(1,5)

try:
    MyFile = open("Favourite.txt" , "r")
    line = MyFile.readline().strip()
    index = 0
    while line != "" and index < row:

        for index in range(0 ,row):
            NumbersColours[index][0] = line
            line = MyFile.readline().strip()
            NumbersColours[index][1] = line
            line = MyFile.readline().strip()
            index += 1
        #print(line)
    MyFile.close()
except IOError:
    print("File does not exist")


def InsertionSort():
    for index in range(0 , len(NumbersColours)):
        temp1 = NumbersColours[index][0]
        temp2 = NumbersColours[index][1]
        current = index - 1
        while NumbersColours[index][0] > temp1 and current >= 0:
            NumbersColours[current + 1] = NumbersColours[current]
            current = current - 1
    NumbersColours[current + 1] = temp1
    NumbersColours[current + 1] = temp2

# NumbersColours = [[4 , "green"] , [7 , "orange"] , [2 , "white"]]

def OutputAll():
    for index in range(col):
        print(Players[index] , "Players are playing. Theme is" , NumbersColours[index][1] , ". Import colour pallette#" , NumbersColours[index][0])

def BubbleSort():
    top = len(Players) - 1
    index = 0
    swap = True
    while swap:
        swap = False
        for index in range(0 , top):
            if Players[index + 1] > Players[index]:
                temp = Players[index]
                Players[index] = Players[index + 1]
                Players[index + 1] = temp
        top = top - 1
        OutputAll()

print(Players)
print(NumbersColours)
OutputAll()
BubbleSort()