array = [6, 13, 20, 10, 18, 22, 14, 8, 24]


def total():
    index = 0
    sum = 0
    for index in range(0, len(array)):
        sum = sum + array[index]
    return sum


print(total())
