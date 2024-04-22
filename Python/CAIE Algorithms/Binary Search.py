array = [6, 8, 10, 13, 14, 18, 20, 22, 24] # Sorted array 

def BinarySearch(SearchItem):

    found = False
    SearchFalied = False
    First = 0
    Last = len(array)

    while not(found) and not(SearchFalied):
        middle = (First + Last) // 2
        if array[middle] == SearchItem:
            found = True
        elif First >= Last:
            SearchFalied = True
        elif array[middle] > SearchItem:
            Last = middle - 1
        else:
            First = middle + 1
    
    if found == True:
        print("Item found at index " , middle)
    else:
        print("Item does not exist")

BinarySearch(int(input("Input the item you want to search: ")))
