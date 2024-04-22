#Declare an array DataArray with 100 elements of integer type initialized with 0
DataArray = [0]*100

def ReadFile():
    try:
        MYFILE = open("IntegerData.txt" , "r")
        line = MYFILE.readline().strip()
        while line != "":
           for i in range(0,len(DataArray)):
                DataArray[i] = int(line)
                line = MYFILE.readline().strip()
    except IOError:
        print("Error: File not found")
    
def FindValues():
    Num = int(input("Input a value to search: "))
    if Num > 100 or Num < 0:
        print("Error: Number must be between 0 and 100")
        FindValues()
    else:
        index = 0
        Occurances = 0
        maxindex = len (DataArray) - 1
        while index <= maxindex:
            if DataArray[index] == Num:
                Occurances +=1
            index = index + 1
    return Occurances

def BubbleSort():
    top = len(DataArray)
    swap = True
    while swap:
        swap = False
        for index in range(0 , top-1):
            if DataArray[index] > DataArray[index + 1]:
                temp = DataArray[index]
                DataArray[index] = DataArray[index + 1]
                DataArray[index + 1] = temp
                swap = True
        top = top - 1

ReadFile()
SearchResult = FindValues()
print("The Number you entered occurs" , SearchResult , "times.")
BubbleSort()
print(DataArray)
#print(DataArray)