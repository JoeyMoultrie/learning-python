# Joey Moultrie: August 20, 2026
# Simple program to generate the first 10 cubes using a list comprehension.

# The list of cubes utilizing a list comprehension to do it
cubed = [cube**3 for cube in range(1, 11)]

# For loop to print the list
for cube in cubed:
    print(cube)
