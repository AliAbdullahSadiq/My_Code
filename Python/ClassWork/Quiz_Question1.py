# 16 Feb 2024

def RecursiveValue(Number , ToFind):
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)
        # EndIF
    # EndIF    
# EndFunction
        
print(RecursiveValue(30,30))
print(RecursiveValue(360,360))