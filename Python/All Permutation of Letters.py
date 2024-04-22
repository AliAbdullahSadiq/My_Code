from itertools import product

# Given letters
letters = "EBONYJAMIAH"

# Specify lengths for the two strings
length_1 = 5
length_2 = 6

# Generate all combinations
combinations = [''.join(combination) for combination in product(letters, repeat=length_1 + length_2)]

# Print the combinations
for combo in combinations:
    print(combo[:length_1], combo[length_1:])