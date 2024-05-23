queue = ["" for _ in range(7)]
head = -1
tail = -1
max_size = 6

def Enqueue(item):
    global head, tail
    if (head == 0 and tail == max_size) or (head == tail + 1):
        print("Queue is full")
    else:
        if head == -1:
            head = 0
        tail = (tail + 1) % (max_size + 1)
        queue[tail] = item

def Dequeue():
    global head, tail
    if head == -1:
        print("Queue is empty")
    else:
        item = queue[head]
        if head == tail:
            head = -1
            tail = -1
        else:
            head = (head + 1) % (max_size + 1)
        return item

def UI():
    print("Do you want to enqueue or dequeue?")
    user_input = input("Enter: ").lower()
    if user_input == "enqueue":
        item = input("Enter item: ")
        Enqueue(item)
    elif user_input == "dequeue":
        item = Dequeue()
        if item != "":
            print("Dequeued item:", item)
    else:
        print("Invalid input")
        UI()

UI()