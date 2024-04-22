Name = [[""] * 5 for a in range(2)]
Score = [0]*5

def Populate():
    
    try:
        MyFile = open("Scores.txt", "r")
        line = MyFile.readline().strip()
        index = 0
        while line != "":
            Score[index] = int(line)
            index += 1
            line = MyFile.readline().strip()
        MyFile.close()
    except IOError:
        print("File does not exist")

    for i in range(2):
        for j in range(5):
            Name[i][j] = input(f"Enter a name for player {i+1}, with the last name {j+1}: ")

def Sort():
    YearSize = 5
    Flag = True

    while Flag:
        Flag = False
        for Student in range(YearSize - 1):
            if Score[Student] < Score[Student + 1]:
                Temp1 = Score[Student]
                Temp2 = Name[0][Student]
                Temp3 = Name[1][Student]

                Score[Student] = Score[Student + 1]
                Name[0][Student] = Name[0][Student + 1]
                Name[1][Student] = Name[1][Student + 1]

                Score[Student + 1] = Temp1
                Name[0][Student + 1] = Temp2
                Name[1][Student + 1] = Temp3

                Flag = True

    print("Sorted Scores:")
    print(Score)
    print("Sorted Names:")
    for i in range(2):
        name_str = "[" + ", ".join(Name[i]) + "]"
        print(name_str)

Populate()
Sort()
#print(Score)
#print(Name)