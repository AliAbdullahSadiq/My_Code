MyList = []
NullPtr = -1
StartPtr = -1
FreePtr = -1

class Node:
    def __init__(self, d, p):
        self.data = d
        self.pointer = p

def Initialization():
    for i in range(0, 6):
        MyList.append(Node("", i + 1))
    
    MyList.append(Node("", NullPtr))

def OutputGrid():
    for i in range(0, 5):
        print(i , " " , MyList[i].data , " " , MyList[i].pointer)

def OutputAllNodes():
    global CurrentPtr, StartPtr
    CurrentPtr = StartPtr

    while CurrentPtr != NullPtr:
        print(MyList[CurrentPtr].data)
        CurrentPtr = MyList[CurrentPtr].pointer

def FindNode(DataItem):
    global CurrentPtr, StartPtr
    CurrentPtr = StartPtr
    while CurrentPtr != NullPtr and MyList[CurrentPtr].data != DataItem: # While the data isn't DataIem and not end of list
        CurrentPtr = MyList[CurrentPtr].pointer                          # Increment CurrentPtr

    if MyList[CurrentPtr].data == DataItem:
        print("Item found at node", CurrentPtr)
    else:
        print("Item not found")

def DeleteNode():
    global CurrentPtr, StartPtr
    ThisNode = StartPtr

    DataItem = input("Input the data you want to delete: ")

    while ThisNode != NullPtr and MyList[ThisNode].data != DataItem:
        PrevNode = ThisNode
        ThisNode = MyList[ThisNode].pointer
    
    if ThisNode != NullPtr:
        if StartPtr == ThisNode:
            StartPtr = MyList[StartPtr].pointer
        else:
            MyList[PrevNode].pointer = MyList[ThisNode].pointer
    else:
        print("Item is not in the list")

def InsertNode(NewItem):
    global FreePtr, StartPtr

    if FreePtr == NullPtr:
        print("Error: no space for insert!")
    else:
        NewNodePtr = FreePtr               # Prepare to insert (create a node, add it to the list)
        MyList[NewNodePtr].data = NewItem
        FreePtr = MyList[FreePtr].pointer

        if StartPtr == NullPtr: # If the data is the first item inserted to the list
            StartPtr = NewNodePtr
        else:
            ThisNodePtr = StartPtr
            while MyList[ThisNodePtr].pointer != NullPtr:
                ThisNodePtr = MyList[ThisNodePtr].pointer
            MyList[ThisNodePtr].pointer = NewNodePtr

Initialization()
OutputGrid()
OutputAllNodes()
FindNode("error value")
InsertNode(input("Input the item you want to insert: "))
DeleteNode()
OutputGrid()
OutputAllNodes()