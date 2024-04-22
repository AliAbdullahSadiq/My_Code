import time
start = time.time()

# DECLARE array : ARRAY[0:7] OF INTEGER
array = [6, 13, 20, 10, 18, 22, 14, 8, 24]

print(array)

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

print(array)

end = time.time()
print(end - start)