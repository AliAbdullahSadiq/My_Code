# Global array size 7, index 0 to 6, data type node
MyList = []
NullPointer = -1
StartPointer = -1
FreeListPtr = 0

class Node:
    def __init__(self, d, p):
        self.data = d
        self.pointer = p

def initialisation():
    global FreeListPtr, StartPointer
    for index in range(0, 6):
        MyList.append(Node("", index + 1))
    
    MyList.append(Node("", NullPointer))
    FreeListPtr = 0
    StartPointer = NullPointer

def findNode(DataItem):
    CurrentNodePtr = StartPointer
    while CurrentNodePtr != NullPointer and MyList[CurrentNodePtr].data != DataItem:
        CurrentNodePtr = MyList[CurrentNodePtr].pointer

    if MyList[CurrentNodePtr].data == DataItem:
        print("Item found at node", CurrentNodePtr)
    else:
        print("Item not found")

def insertnode(newitem):
    global FreeListPtr, StartPointer
    if FreeListPtr == NullPointer:
        print("Error, no space, the linked list is full")
    else:
        NewNodePtr = FreeListPtr
        MyList[NewNodePtr].data = newitem
        FreeListPtr = MyList[FreeListPtr].pointer

        if StartPointer == NullPointer:
            MyList[NewNodePtr].pointer = NullPointer
            StartPointer = NewNodePtr
        else:
            if newitem < MyList[StartPointer].data:
                MyList[NewNodePtr].pointer = StartPointer
                StartPointer = NewNodePtr
            else:
                ThisNodePtr = StartPointer
                while ThisNodePtr != NullPointer and MyList[ThisNodePtr].data <= newitem:
                    previousNodePtr = ThisNodePtr
                    ThisNodePtr = MyList[ThisNodePtr].pointer

                MyList[NewNodePtr].pointer = MyList[previousNodePtr].pointer
                MyList[previousNodePtr].pointer = NewNodePtr

def DeleteNode(dataitem):
    global FreeListPtr, StartPointer
    ThisNodePtr = StartPointer
    while ThisNodePtr != NullPointer and MyList[ThisNodePtr].data != dataitem:
        previousNodePtr = ThisNodePtr
        ThisNodePtr = MyList[ThisNodePtr].pointer

    if ThisNodePtr != NullPointer:
        if ThisNodePtr == StartPointer:
            StartPointer = MyList[StartPointer].pointer
        else:
            MyList[previousNodePtr].pointer = MyList[ThisNodePtr].pointer
            MyList[ThisNodePtr].pointer = FreeListPtr
            FreeListPtr = ThisNodePtr
    else:
        print("Item to be deleted is not in the linked list")

def OutputGrid():
    print("Index\tData\tPointer")
    for index in range(0, 7):
        print(index, "\t", MyList[index].data, "\t", MyList[index].pointer)
    print("FreeListPtr:", FreeListPtr)
    print()

def OutputAllNodes():
    CurrentNodePtr = StartPointer
    while CurrentNodePtr != NullPointer:
        print(MyList[CurrentNodePtr].data)
        CurrentNodePtr = MyList[CurrentNodePtr].pointer

# Initialize
print("Initialize")
initialisation()
OutputGrid()

# Insert
print("Insert")
insertnode(13)
insertnode(12)
insertnode(34)
insertnode(56)
insertnode(90)
insertnode(65)
insertnode(3)
OutputGrid()

insertnode(2)

# Delete
print("Delete 13")
DeleteNode(13)
OutputGrid()
OutputAllNodes()
