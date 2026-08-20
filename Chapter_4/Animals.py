# Joey Moultrie: August 19, 2026
# Simple program working with lists in Python

# Create a list of animals with something in common
animals = ['dogs', 'wolves', 'foxes']

# For loop to print the items in the list
for animal in animals:
    print(animal.title(), end = " ")
    
# Print specific messages about each list item.
print(f"\n\n{animals[0].title()} make great pets.\n{animals[1].title()} are fierce predators.\nThe slyest animals are {animals[2]}.")

# Print a line about what each animal has in common.
print("\nAll of these animals are canids.")

