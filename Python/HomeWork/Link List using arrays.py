DataArray = []
PtrArray = []
NullPtr = -1
FreePtr = -1
StartPtr = -1

class Node:
    def __init__(self, d, p):
        self.data = d
        self.pointer = p

def Initialization():
    global DataArray, PtrArray, FreePtr, StartPtr
    for i in range(0, 6):
        DataArray.append("")
        PtrArray.append(i + 1)

    PtrArray.append(NullPtr)
    FreePtr = 0

def OutputGrid():
    global DataArray, PtrArray
    for i in range(0, 5):
        print(i, " ", DataArray[i], " ", PtrArray[i])

def OutputAllNodes():
    global DataArray, PtrArray, StartPtr
    CurrentPtr = StartPtr

    while CurrentPtr != NullPtr:
        print(DataArray[CurrentPtr])
        CurrentPtr = PtrArray[CurrentPtr]

def FindNode(DataItem):
    global DataArray, PtrArray, StartPtr
    CurrentPtr = StartPtr
    while CurrentPtr != NullPtr and DataArray[CurrentPtr] != DataItem:
        CurrentPtr = PtrArray[CurrentPtr]

    if DataArray[CurrentPtr] == DataItem:
        print("Item found at node", CurrentPtr)
    else:
        print("Item not found")

def DeleteNode():
    global DataArray, PtrArray, StartPtr
    ThisNode = StartPtr

    DataItem = input("Input the data you want to delete: ")

    while ThisNode != NullPtr and DataArray[ThisNode] != DataItem:
        PrevNode = ThisNode
        ThisNode = PtrArray[ThisNode]

    if ThisNode != NullPtr:
        if StartPtr == ThisNode:
            StartPtr = PtrArray[StartPtr]
        else:
            PtrArray[PrevNode] = PtrArray[ThisNode]
            PtrArray[ThisNode] = FreePtr
            FreePtr = ThisNode
    else:
        print("Item is not in the list")

def InsertNode(NewItem):
    global DataArray, PtrArray, FreePtr, StartPtr
    if FreePtr == NullPtr:
        print("Error, no space, the linked list is full")
    else:
        NewNodePtr = FreePtr
        DataArray[NewNodePtr] = NewItem
        FreePtr = PtrArray[FreePtr]

        if StartPtr == NullPtr:
            PtrArray[NewNodePtr] = NullPtr
            StartPtr = NewNodePtr
        else:
            if NewItem < DataArray[StartPtr]:
                PtrArray[NewNodePtr] = StartPtr
                StartPtr = NewNodePtr
            else:
                ThisNodePtr = StartPtr
                while ThisNodePtr != NullPtr and DataArray[ThisNodePtr] <= NewItem:
                    previousNodePtr = ThisNodePtr
                    ThisNodePtr = PtrArray[ThisNodePtr]

                PtrArray[NewNodePtr] = PtrArray[previousNodePtr]
                PtrArray[previousNodePtr] = NewNodePtr

Initialization()
OutputGrid()
OutputAllNodes()
FindNode("error value")
InsertNode("gobbledy gook")
DeleteNode()
OutputGrid()
OutputAllNodes()