import time
start = time.time()

# DECLARE array : ARRAY[0:7] OF INTEGER
array = [6, 13, 20, 10, 18, 22, 14, 8, 24]

print(array)

def insertion():
    # DECLARE temp, current, index : INTEGER
    for index in range(1, len(array)):
        temp = array[index]
        current = index - 1
        while (current >= 0) and array[current] > temp:
            array[current + 1] = array[current]
            current = current - 1
        array[current + 1] = temp

insertion()
print(array)

end = time.time()
print(end - start)