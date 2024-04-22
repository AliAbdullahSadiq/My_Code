class Node:
    def __init__(self, d, l, r):
        self.data = d
        self.leftptr = l
        self.rightptr = r

def Initialization():
    global MyList, NullPointer, rootptr, FreeListPtr
    MyList = []
    NullPointer = -1
    rootptr = -1
    FreeListPtr = 0
    for Index in range(0, 7):
        MyList.append(Node(0, Index+1, -1))
    MyList.append(Node(0, -1, -1))

def findNode(DataItem):
    global MyList, NullPointer, rootptr, FreeListPtr
    CurrentNodePtr = rootptr
    while CurrentNodePtr != NullPointer and MyList[CurrentNodePtr].data != DataItem:
        if MyList[CurrentNodePtr].data > DataItem:
            CurrentNodePtr = MyList[CurrentNodePtr].leftptr
        else:
            CurrentNodePtr = MyList[CurrentNodePtr].rightptr

    if CurrentNodePtr != NullPointer and MyList[CurrentNodePtr].data == DataItem:
        print("Item found at node ", CurrentNodePtr)
    else:
        print("Item not found")

def Insert(Item):
    global MyList, NullPointer, rootptr, FreeListPtr
    if FreeListPtr == NullPointer:
        print("Error! Tree is full")
    else:
        # Prepare to insert
        NewNodePtr = FreeListPtr # Copy FreeListPtr
        MyList[NewNodePtr].data = Item
        FreeListPtr = MyList[FreeListPtr].leftptr # inc FreeListPtr
        MyList[NewNodePtr].leftptr = NullPointer
        MyList[NewNodePtr].rightptr = NullPointer

        # Case A: Inserting root
        if rootptr == NullPointer:
            rootptr = NewNodePtr
        else:
            # Case B: Find where to insert
            ThisNodePtr = rootptr
            while ThisNodePtr != NullPointer:
                PreviousNodePtr = ThisNodePtr # Keep track of previous pointer
                if MyList[ThisNodePtr].data > Item:
                    TurnedLeft = True
                    ThisNodePtr = MyList[ThisNodePtr].leftptr
                else:
                    TurnedLeft = False
                    ThisNodePtr = MyList[ThisNodePtr].rightptr

            if TurnedLeft:
                MyList[PreviousNodePtr].leftptr = NewNodePtr
            else:
                MyList[PreviousNodePtr].rightptr = NewNodePtr

def output():
    global MyList, NullPointer, rootptr, FreeListPtr
    print("Index\tData\tLeftPtr\tRightPtr")
    for i in range(0, 7):
        print(i, '\t', MyList[i].data, '\t', MyList[i].leftptr, '\t', MyList[i].rightptr)
    print("rootptr ", rootptr)
    print("freeListPtr ", FreeListPtr)
    print()

def Inorder(ThisNodePtr):
    global MyList, NullPointer, rootptr, FreeListPtr
    if ThisNodePtr != NullPointer:
        Inorder(MyList[ThisNodePtr].leftptr)
        print(MyList[ThisNodePtr].data)
        Inorder(MyList[ThisNodePtr].rightptr)

print("initialise")
Initialization()
output()
print("insert")
Insert("Cat")
Insert("Dog")
Insert("Book")
Insert("Bag")
Insert("Chair")
Insert("Birds")
Insert("Lamp")
output()
print("Inorder traversal")
Inorder(rootptr)