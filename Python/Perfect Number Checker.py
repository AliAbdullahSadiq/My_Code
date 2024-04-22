def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def perfect_numbers_up_to(limit):
    perfect_numbers = []
    p = 2
    while True:
        perfect_num = (1 << (p - 1)) * ((1 << p) - 1)
        if perfect_num > limit:
            break
        if is_prime((1 << p) - 1):
            perfect_numbers.append(perfect_num)
        p += 1
    return perfect_numbers

def main():
    try:
        limit = int(input("Enter the limit to check for perfect numbers: "))
        #limit = 10**72
        if limit < 2:
            print("Limit should be at least 2.")
            return
        perfect_nums = perfect_numbers_up_to(limit)
        if perfect_nums:
            print("Perfect numbers found are:")
            print(perfect_nums)
        else:
            print("No perfect numbers found")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()
