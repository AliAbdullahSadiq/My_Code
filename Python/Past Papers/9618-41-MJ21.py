# Declare an Array named arrayData with 10 elements
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

userInput = int(input("Enter the number to search: "))

def linearSearch(value):
   
    #Declare an integer index and a boolean found
    index = 0
    found = False

    while found == False and index < 10: 
        if arrayData[index] == value:
            found = True
        else: 
            index = index + 1
        #ENDIF
    #ENDWHILE

    if found == True:
        return True
    else: return False
#ENDFUNCTION

print(linearSearch(userInput))