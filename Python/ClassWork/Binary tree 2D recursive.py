class Node:
    def __init__(self, d, l, r):
        self.data = d
        self.LeftPointer = l
        self.RightPointer = r


ArrayNodes = [] # 20 elements of nodes 

ArrayNodes.append(Node(10, -1, 2))
ArrayNodes.append(Node(5, -1, -1))
ArrayNodes.append(Node(16, -1, -1))

for i in range (3,19):
    ArrayNodes.append(Node(0, i+1, -1))
ArrayNodes.append(Node(0, -1, -1))

RootPointer = -1 # type integer
FreeNodes = 0 # type integer

def AddNode():


AddNode()