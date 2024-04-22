rows = 10
cols = 5

import random

array = [[0]* cols for i in range(rows)]
print(array)

r = 0
c = 0

for r in range(rows):
    for c in range(cols):
        array[r][c] = random.randint(0, 10)

print(array)