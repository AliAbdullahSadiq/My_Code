import random

def initialize_2d_array(rows, cols):
    array_data = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return array_data

def print_2d_array(array):
    for row in array:
        for element in row:
            print(element, end='\t')
        print()

def bubble_sort_2d_array(array):
    rows = len(array)
    cols = len(array[0])

    for x in range(rows):
        for y in range(cols - 1):
            for z in range(cols - y - 1):
                if array[x][z] > array[x][z + 1]:
                    temp_value = array[x][z]
                    array[x][z] = array[x][z + 1]
                    array[x][z + 1] = temp_value

# def main():
row = 10
col = 10

ArrayData = initialize_2d_array(row, col)

print("Unsorted Array:")
print_2d_array(ArrayData)

bubble_sort_2d_array(ArrayData)

print("\nSorted Array:")
print_2d_array(ArrayData)