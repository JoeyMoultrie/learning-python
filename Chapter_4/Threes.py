# Joey Moultrie: Auguast 20, 2026
# Program to create a list of the multiples of three.

# List of the threes
multipliers = list(range(3, 31))
threes = []

for multiple in multipliers:
    threes.append(multiple * 3)

# Loop printing the threes
for three in threes:
    print(three, end = ' ')
    

