# Joey Moultrie: August 20, 2026
# Simple program using a tuple

# Create a tuple with 5 foods served at a restaurant
menu = ('soup', 'salad', 'chicken', 'bread', 'desert')

print("The Menu Is:")
for food in menu:
    print(food.title())

print("\nThe New Menu Is:")

menu = ('soup', 'salad', 'chicken', 'potatoes', 'biscuits')
for food in menu:
    print(food.title())