def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0    # Base case
    elif Value[0] in 'aeiou':
        return RecursiveVowels(Value[1:]) + 1
    else:
        return RecursiveVowels(Value[1:]) + 0
    
print(RecursiveVowels(input("Input the String: ")))