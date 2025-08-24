

import random

# Generate your numbers
my_numbers = [random.randint(1, 69) for _ in range(5)] + [random.randint(1, 26)]
print("My numbers:", my_numbers)

count = 1  # Start with first draw
# Generate initial winning numbers
winning_numbers = [random.randint(1, 69) for _ in range(5)] + [random.randint(1, 26)]
print("Initial winning numbers:", winning_numbers)

# Keep drawing until we match
while my_numbers != winning_numbers:
    winning_numbers = [random.randint(1, 69) for _ in range(5)] + [random.randint(1, 26)]
    count += 1

print("It took", count, "draws to match the numbers!")