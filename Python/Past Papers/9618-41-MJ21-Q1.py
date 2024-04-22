class Node:
    def __init__(self, d, n):
        self.data = d
        self.nextNode = n

def initialization():
    linkedList = []
    linkedList.append(Node(1, 1))
    linkedList.append(Node(5, 4))
    linkedList.append(Node(6, 7))
    linkedList.append(Node(7, -1))
    linkedList.append(Node(2, 2))
    linkedList.append(Node(0, 6))
    linkedList.append(Node(0, 8))
    linkedList.append(Node(56, 3))
    linkedList.append(Node(0, 9))
    linkedList.append(Node(0, -1))

    return linkedList

def outputNodes(linkedList):
    currentPtr = linkedList[0].nextNode

    while currentPtr != -1:
        print(linkedList[currentPtr].data)
        currentPtr = linkedList[currentPtr].nextNode

def addNode(linkedList, emptyList):
    newData = int(input("Input the data to be added: "))

    if emptyList >= len(linkedList):
        print("Error: no space for insert!")
        return False

    newNodePtr = emptyList
    linkedList[newNodePtr].data = newData
    emptyList += 1

    return True, emptyList

# main
linkedList = initialization()
startPointer = 0
emptyList = 5

print("Initial Nodes:")
outputNodes(linkedList)

b , emptyList = addNode(linkedList, emptyList)

if b:
    print("Node added successfully!")
else:
    print("Failed to add node.")

print("Nodes after adding a new node:")
outputNodes(linkedList)