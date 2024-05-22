class ClassName:
    def __init__(self, attribute1, attribute2):  # Constructor
        self.__attribute1 = attribute1
        self.__attribute2 = attribute2

    def get_attribute1(self):  # Getter
        return self.__attribute1
    
    def get_attribute2(self):  # Getter
        return self.__attribute2
    
I_AM_OBJECT = ClassName("DataType", "DataType")  # Object

Give_Me_Attribute1 = I_AM_OBJECT.get_attribute1
Give_Me_Attribute2 = I_AM_OBJECT.get_attribute2

print(Give_Me_Attribute1())
print(Give_Me_Attribute2())