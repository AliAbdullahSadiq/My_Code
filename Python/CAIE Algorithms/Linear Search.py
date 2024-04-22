# DECLARE array : ARRAY[0:7] OF INTEGER
array = [2, 3, 17, 22, 29, 31, 34, 40]

# DECLARE num : INTEGER
# DECLARE index : INTEGER
# DECLARE found : BOOLEAN
# DECLARE maxindex : INTEGER

index = 0
found = False

num = int(input("Enter the number you wanna search: "))

maxindex = len(array) - 1
while found == False and index <= maxindex:
    if array[index] == num:
        found = True
    else:
        index = index + 1

if found == True:
    print("Found at address: ", index + 1)
else:
    print("Item does not exist.")