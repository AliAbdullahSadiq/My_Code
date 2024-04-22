# Q1:

def Count(Number):
    if Number % 2 != 0:
        Number -= 1
    print(Number)
    if Number > 0:
         return Count(Number)

Count(25)

# Q3:

Base = 0
Power = 0

def FindPower(Base, Power):
    if Power == 0:  # Base case
        return 1
    else:
        return Base * FindPower(Base, Power - 1)

result = FindPower(2, 4)
print(result)

