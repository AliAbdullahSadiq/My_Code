import random

array = []

for x in range(1, 10):
    array.append(random.randint(1,10))

array.sort()

print(array)