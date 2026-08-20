# Joey Moultrie: August 19, 2026
# A program creating a list and then min(), max(), and sum() functions to check values in list and add them together

# Creating the list
million = list(range(1, 1000001))

print(min(million))
print(max(million))
print(sum(million))

# Using slicing to interact with parts of a list
print("The first three numbers in the list are:")
for number in million[:3]:
    print(number)

# Using slicing to print the 3 middle numbers in the list
print("The three middle numbers in the list are:")
for number in million[499998:500001]:
    print(number)

# Using slicing to print the last 3 numbers in the list
print("The last three numbers in the list are:")
for number in million[-3:]:
    print(number)