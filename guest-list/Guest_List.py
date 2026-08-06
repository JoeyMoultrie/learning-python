# Joey Moultrie: August 5, 2027
# A list created of those I would like to have a dinner with, living or dead and then printing a message to each.
# There is a scenario playing throughout the code that is outlined in the notes. 
# This is practice using lists.

guests = ['Gen. William Moultrie', 'Ken Block', 'Dad', 'Timber-Ky']
print("PART ONE")
# Create a loop to print a message to each guest inviting them to dinner.
for guest in guests:
    print(f"\nHi {guest}, I would like to invite you to dinner at my house. Please RSVP as soon as possible so I can make plans.\nHope to hear from you soon.")

print("\n\n")
# Change in plans. I had one gues say they couldn't come. Need to inform the others of the change and then remove the guest who can't come.
# Add a new guest to the list and send out new invitations to the updated guest list.

# Remove the guest who can't come and store them in a variable.
cant_come = 'Gen. William Moultrie'
guests.remove(cant_come)

print("PART TWO")
# Loop to inform guest of the change in who's coming to dinner.
for guest in guests:
    print(f"\nHI {guest}, I heard back from {cant_come} and he said he can't come. Heh's too busy fighting the British. I will let you know who will be coming in his stead soon.")

print("\n\n")

# Add a new guest to the list and send out new invitations.
new_guest = 'JRR Tolkien'
guests.append(new_guest)

print("PART THREE")
# Loop for the new invitations.
for guest in guests:
    print(f"\nHi {guest}, I am inviting to you dinner at my house next Saturday. Hope to see you there. If you can't make it, let me know")

print("\n\n")

print("PART FOUR")
# I found a bigger table so I can invite three more guests to dinner.
for guest in guests:
    print(f"\nHi {guest}, I just got a bigger table so I will be inviting more people to our dinner party.")

print("\n\n")

print("PART FIVE")
# Using insert() and append() methods to add the three additional guests.
guests.insert(0, 'Sebastian Ogier') # Insert a new guest at the biggining of my list.
guests.insert(2, 'Derek Jeter') # Insert new guest to the middle of my list.
guests.append('Ernest Shackleton') # Insert new guest at the end of my list.

# Print new invites to all my guests.
for guest in guests:
    print(f"\nHello {guest}, you are invited to come to dinner at my house this weekend. I'm excited to see you there.")

print("\n\n")

print("PART SIX")
# This has been a wild ride trying to get people invited to dinner at my house. Now my new table won't show up and I can only invite two guests.
# I will use the pop() method to remove guests from my list until only two remnain.

while len(guests) > 2:
    guests.pop(0)

for guest in guests:
    print(f'\nLuckily {guest}, you are still invited to dinner at my house.')
