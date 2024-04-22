# DECLARE x, y: INTEGER

x = int(input('x = '))
y = int(input('y = '))

def Unknown(x, y):
    if x < y:
        print(x + y)
        return Unknown(x + 1, y) * 2
    elif x == y:
        return 1
    else:
        print(x + y)
        return Unknown(x - 1, y) // 2
    # ENDIF
# ENDFUNCTION

print(10)
print(15)
print(Unknown(10, 15))

print('----------------------------------------------------------------')

print(10)
print(10)
print(Unknown(10, 10))

print('----------------------------------------------------------------')

print(15)
print(10)
print(Unknown(15, 10))

# ------------------------------------------------------------------------------------------------------------------------

def IterativeUnknown():

    while X < Y:
        print(X + Y)
        X += 1
        Y = Y
        Y = Y * 2

    if X == Y:
        return 1
    else:
        print(X + Y)
        X -= 1
        Y = Y
        Y = Y // 2
        return result

IterativeUnknown(x, y)