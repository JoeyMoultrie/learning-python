# Joey Moultrie: August 20, 2026
# Simple program to generate a list of cubes from 1 - 10.

# Creating the list.
cubes = list(range(1, 11)) # Values to be cubed
cubed =[] # The list of cubed values

# Loop to store cubed values in cubed
for cube in cubes:
    cubed.append(cube ** 3)

# Loop to print cubed values.
for cube in cubed:
    print(cube)
