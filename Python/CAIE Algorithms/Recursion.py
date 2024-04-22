def factorial_recursive(n):
    # Base case
    if n == 0:
        return 1
    # General case
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print("Factorial of", number, "is", factorial_recursive(number))

number = 5
print("Factorial of", number, "is", factorial_iterative(number))
