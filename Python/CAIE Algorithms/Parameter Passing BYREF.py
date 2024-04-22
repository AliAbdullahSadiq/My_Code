# Procedure to demonstrate BYREF parameter passing
def test(x, y, z, t):  # PROCEDURE test(BYREF x, BYREF y, BYREF z, BYVAL t)
    # Increment each parameter by 1
    x += 1
    y += + 1
    z += + 1
    t += + 1

    # Return the modified values of x, y, and z
    return x, y, z  # Not returning t

# main
# Initial values
x = 2
y = 3
z = 6
t = 4

# Call the test procedure with parameters x, y, z, t
a, b, c = test(x, y, z, t)  # Correct usage

# Output the results
print("Modified values:")
print("x :", a)  # Output the modified value of x
print("y :", b)  # Output the modified value of y
print("z :", c)  # Output the modified value of z
print("t :", t)  # Output the original value of t (not modified)
