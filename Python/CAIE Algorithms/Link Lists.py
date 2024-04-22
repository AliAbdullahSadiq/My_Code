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
    while CurrentPtr != NullPtr and MyList[CurrentPtr].data != DataItem: # While the data isn't DataItem and not end of list
        CurrentPtr = MyList[CurrentPtr].pointer                          # Increment CurrentPtr

    if MyList[CurrentPtr].data == DataItem:
        print("Item found at node", CurrentPtr)
    else:
        print("Item not found")

def DeleteNode():
    global CurrentPtr, StartPtr
    ThisNode = StartPtr

    DataItem = input("Input the data you want to delete: ")

    while ThisNode != NullPtr and MyList[ThisNode].data != DataItem: # Same thing as Finding
        PrevNode = ThisNode                                          # Keeping track of the previous node
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
        print("Error, no space, the linked list is full")
    else:
        NewNodePtr = FreePtr                # Copy FreePtr
        MyList[NewNodePtr].data = NewItem   # Prepare to insert (create a node, add it to the list)
        FreePtr = MyList[FreePtr].pointer

        if StartPtr == NullPtr: # If item is the first to be addded
            MyList[NewNodePtr].pointer = NullPtr
            StartPtr = NewNodePtr
        else:
            if NewItem < MyList[StartPtr].data: # If item is the smallest item
                MyList[NewNodePtr].pointer = StartPtr
                StartPtr = NewNodePtr
            else:
                ThisNodePtr = StartPtr
                while ThisNodePtr != NullPtr and MyList[ThisNodePtr].data <= NewItem: # Otherwise, traverse the
                    previousNodePtr = ThisNodePtr                                     # list and find proper place
                    ThisNodePtr = MyList[ThisNodePtr].pointer

                MyList[NewNodePtr].pointer = MyList[previousNodePtr].pointer
                MyList[previousNodePtr].pointer = NewNodePtr

Initialization()
OutputGrid()
OutputAllNodes()
FindNode("error value")
InsertNode("gobbledy gook")
DeleteNode()
OutputGrid()
OutputAllNodes()