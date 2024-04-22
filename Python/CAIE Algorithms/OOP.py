class ClassName:
    def __init__(self , attribute1 , attribute2): # Constructor
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def GetAttribute1(self): # Getter
        return self.attribute1
    
    def GetAttribute2(self): # Getter
        return self.attribute2
    
I_AM_OBJECT = ClassName("DataType" , "DataType") # Object

Give_Me_Attribute1 = I_AM_OBJECT.GetAttribute1
Give_Me_Attribute2 = I_AM_OBJECT.GetAttribute2

print(Give_Me_Attribute1)
print(Give_Me_Attribute2)
