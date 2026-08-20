# Joey Moultrie: August 18, 2026
# A simple loop program to practice creating a for loop to iterate over a list. Practice indentation within and without the list.
# Practice copying the list

# A loop to print my favorite pizzas.
pizzas = ['pepperoni', 'hot honey pepperoni', 'hawaiian', 'meat-lovers']
for pizza in pizzas:
    print(f"I really like {pizza.title()} pizza!")

print("\nI really love pizza.")

# Make a copy of my pizza list and make changes to both
your_pizza = pizzas[:]

# Make a change to the original list without affecting the new list
pizzas.append('sausage')

# Add a piiza to your_pizza list
your_pizza.append('vegitarian')

# Prove that my lists are different
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("Your favorite pizzas are:")
for pizza in your_pizza:
    print(pizza)
