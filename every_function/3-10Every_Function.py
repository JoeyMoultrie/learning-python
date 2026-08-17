# Joey Moultrie: August 15, 2026
# Very simple program that creates a list and then uses each function in the chapter to modify the list

#Create the list. Top 5 tallest mountain peaks in the world
tallest_peaks = ['makalu', 'everest', 'k2', 'lhotse', 'kangchenjunga']

# Print the original list
print("\nTHE ORIGINAL LIST")

# For loop to print the list in a nice format
for peak in tallest_peaks:
    print(peak.title(), end =', ')

# Use list indexs to access certain list items.
print(f"\n\nThe tallest mountain in the world is {tallest_peaks[1].title()}")
print(f"\nThe third tallest mountain is {tallest_peaks[-1].title()}")

# Modifying an element in a list
tallest_peaks[0] = 'denali'

# For loop to print the list in a nice format
print("\nTHE LIST WITH THE FIRST ITEM MODIFIED:")
for peak in tallest_peaks:
    print(peak.title(), end = ', ')

# Use the del statement to remove an item from the list
del tallest_peaks[-1]
print("\n\nTHE LIST WITH ITEMS REMOVED:")
print(f"\n{tallest_peaks}")

# Use the remove by value method to git rid of a known list item
tallest_peaks.remove('denali')
print(f"\n{tallest_peaks}")
# Then add items in.


# Adding items to the beginning, middle, and end of the list
tallest_peaks.insert(0, 'denali')
tallest_peaks.append('makalu')
tallest_peaks.append('kangchenjunga')
tallest_peaks.insert(2, 'mount elbrus')

print("\nTHE LIST WITH ADDED ITEMS")
for peak in tallest_peaks:
    print(peak.title(), end =', ')

# Use the sorted() function to reverse alphabetize the list without modifying the original list variable
print("\n\nREVERSE ALPHABETIZED LIST\nDon't worry, the original is unchanged")

# For loop to print the list in a nice format
for peak in sorted(tallest_peaks, reverse=True):
    print(peak.title(), end = ', ')

# Use the .sort() method to permanently alphabetize the list
print("\n\nALPHABETIZED LIST")

# For loop to print the list in a nice format
# the .sort() method returns None, which cannot be iterated. This means, that before I run the for loop, I need to change the list
# variable. 
# If I try to loop with .sort(), I end up with this error: TypeError: 'NoneType' object is not iterable
tallest_peaks.sort()
for peak in tallest_peaks:
    print(peak, end = ', ')

# Use pop() to print a message about the last peak alphabetically.
hard_spell = tallest_peaks.pop(3)
print(f"\n\n{hard_spell.title()} is too hard to spell so I took it out.")

# Insert that peak back into the list after message is printed.
tallest_peaks.append('kangchenjunga')

# Use the .reverse() method to make my list reverse alphabetized permanently
print("\nREVERSE ALPHABETIZED LIST")
tallest_peaks.reverse() # once again, must reverse the list before I iterate. .reverse() returns 'None'.
for peak in tallest_peaks:
    print(peak, end = ', ')

# Use the len() function to find the length of the current list.
print(f"\n\n{len(tallest_peaks)}")