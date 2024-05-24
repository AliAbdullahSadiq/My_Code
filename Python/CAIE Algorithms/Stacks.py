stack = [None for index in range(0,7)]
basepointer = 0
toppointer = -1
stackfull = 6
item = int(input("Enter the item: "))

def Pop():
    global basepointer, toppointer, item
    if toppointer == -1:
        print("Stack is empty")
    else:
        item = stack[toppointer]
        stack[toppointer] = None  # optional
        toppointer = toppointer - 1
    return item

def Push(item):
    global basepointer, toppointer
    if toppointer < stackfull:
        toppointer = toppointer + 1
        stack[toppointer] = item
    else:
        print("stack full, can't push")

def UI():
    print("do you want to push or pop?")
    userINPUT = input("Enter: ")
    if userINPUT == "pop":
        Pop()
    elif userINPUT == "push":
        INPUT = input("Enter item: ")
        Push(INPUT)
    else:
        print("invalid input")
        UI()

UI()