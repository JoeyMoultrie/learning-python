# Joey Moultrie: August 5, 2027
# A list created of those I would like to have a dinner with, living or dead and then printing a message to each.
# There is a scenario playing throughout the code that is outlined in the notes. 
# This is practice using lists.

guests = ['Gen. William Moultrie', 'Ken Block', 'Dad', 'Timber-Ky']

# Create a loop to print a message to each guest inviting them to dinner.
for guest in guests:
    print(f"\nHi {guest}, I would like to invite you to dinner at my house. Please RSVP as soon as possible so I can make plans.\nHope to hear from you soon.")

# Change in plans. I had one gues say they couldn't come. Need to inform the others of the change and then remove the guest who can't come.
# Add a new guest to the list and send out new invitations to the updated guest list.

# Remove the guest who can't come and store them in a variable.
cant_come = 'Gen. William Moultrie'
guests.remove(cant_come)

# Loop to inform guest of the change in who's coming to dinner.
for guest in guests:
    print(f"\nHI {guest}, I heard back from {cant_come} and he said he can't come. Heh's too busy fighting the British. I will let you know who will be coming in his stead soon.")

# Add a new guest to the list and send out new invitations.
new_guest = 'JRR Tolkien'
guests.append(new_guest)

# Loop for the new invitations.
for guest in guests:
    print(f"\nHi {guest}, I am inviting to you dinner at my house next Saturday. Hope to see you there. If you can't make it, let me know")