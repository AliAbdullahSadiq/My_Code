import time
import random

Bubbletime = 0.0 
Insertiontime = 0.0

def InsertionSort():

    import random
    import time
    start = time.time()

    array = random.sample(range(1, 10001), 10000)


    lowerbound = 0

    for index in range(lowerbound + 1, len(array)):
        temp = array[index]
        current = index - 1
        while (current >= lowerbound) and array[current] > temp:
            array[current + 1] = array[current]
            current = current - 1

        array[current + 1] = temp

    end = time.time()
    print(end - start)

def BubbleSort():
    start = time.time()

    array = random.sample(range(1, 10001), 10000)

    top = len(array)
    swap = True
    while swap:
        swap = False
        for index in range(0, top - 1):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                swap = True
        top = top - 1

    end = time.time()
    print(end - start)

print("Insertion Sort :")
InsertionSort()
print("Bubble Sort :")
BubbleSort()