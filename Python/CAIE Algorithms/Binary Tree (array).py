# Using 1D arrays:

Data = []
Left = []
Right = []
rootpointer = 0  # Assuming the rootpointer is initially set to 0
NullPointer = -1  # Assuming NullPointer is -1

def findNode(searchItem):
    ThisNodePtr = rootpointer
    while ThisNodePtr != NullPointer and Data[ThisNodePtr] != searchItem:
        if Data[ThisNodePtr] > searchItem:
            ThisNodePtr = Left[ThisNodePtr]
        else:
            ThisNodePtr = Right[ThisNodePtr]
    return ThisNodePtr

# Initialization of arrays (assuming size is predefined)
size = 10  # Example size
for _ in range(size):
    Data.append(0)  # Initialize Data array with 0s
    Left.append(NullPointer)  # Initialize Left array with NullPointer
    Right.append(NullPointer)  # Initialize Right array with NullPointer

# Using a 2D array:

Tree = [[0 for _ in range(3)] for _ in range(size)]

def findNode(searchItem):
    ThisNodePtr = rootpointer
    while ThisNodePtr != NullPointer and Tree[ThisNodePtr][0] != searchItem:
        if Tree[ThisNodePtr][0] > searchItem:
            ThisNodePtr = Tree[ThisNodePtr][1]
        else:
            ThisNodePtr = Tree[ThisNodePtr][2]
    return ThisNodePtr

# Initialization of Tree array (assuming size is predefined)
for i in range(size):
    for j in range(3):
        Tree[i][j] = 0  # Initialize Tree array with 0s