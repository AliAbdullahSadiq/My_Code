# Practice question
# Read the IDs and names of customers from Customers.txt into a 2D array - 4 rows and 2 columns

# Constant file name
# Note: Python convention is to write constant identifiers using uppercase only.
# The values can be changed, although you should treat constants as not changeable.

FILENAME = "Customers.txt"

# Global 2D array STRING
row = 4
col = 2
My2DArray = [[""] * col for i in range(row)]

# Note: My2DArray = [[""] * col] * row] produces unexpected behavior
# It doesn't really work because you end up with 4 copies of the same list,
# so when you modify one of them, they all change

print(My2DArray)

# Note: shift + tab and tab to indent left and right

# Method 1
try:
    file = open(FILENAME, "r")
    for count in range(4):  # loop 0 to 3
        My2DArray[count][0] = file.readline().strip()
        My2DArray[count][1] = file.readline().strip()
    file.close()
except:
    print("File not found")

print(My2DArray)

for row in range(4):
    print(My2DArray[row][0], " ", My2DArray[row][1])

# ------------------------------------------------------
# Multi-line comments using '''
#'''
# Method 2 - This section is commented out
#'''
#'''
# try:
#     file = open(FILENAME, "r")
#     count = 0
#     line = file.readline().strip()
#     while line != "" and count <= 3:
#         My2DArray[count][0] = line
#         My2DArray[count][1] = file.readline().strip()
#         line = file.readline().strip()
#         count += 1
#     file.close()
# except:
#     print("File not found")

# print(My2DArray)

# for row in range(4):
#     print(My2DArray[row][0], " ", My2DArray[row][1])
