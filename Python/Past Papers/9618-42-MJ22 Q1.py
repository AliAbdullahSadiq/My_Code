#Declare a global array of 10 integers called StackData
#Declare a global variable called StackPointer of type integer
#StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#StackData = [12, 32, 23, 23, 34, 34, 34, 34, 54, 45, 23]
StackData = [12, 32, 23, 23, 34, 34, 34, 34, 54, 45, 0]
StackPointer = 0

def OutputValues():
    print(StackData)
    print(StackPointer)

def Push(PushNum):
    flag = False
    StackPointer = 0
    while StackPointer != 10 and flag == False:
        if StackData[StackPointer] == 0:
            StackData[StackPointer] = PushNum
            flag = True
        else:
            StackPointer = StackPointer + 1
    return flag
    
for i in range(0,11):
    PushNum = int(input("Enter the number you want to push: "))
    if Push(PushNum) == True:
        print("You have pushed")
    else: print("You have not pushed; The stack is full!")
OutputValues()