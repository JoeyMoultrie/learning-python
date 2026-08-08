# Joey Moultrie: August 8, 2026
# A basic project to convert temperature to Fahrenheit or Celsius.

def main():
    # Get user input for temperature scale and current temperature to convert.
    temp_scale = input("What temperature scale do you want to convert to? Enter 'f' for Fahrenheit and 'c' for Celsius: ")
    current_temp = float(input("What is the current temperature you want to convert? "))

    # Convert to Fahrenheit if that is what user wants.
    
    if temp_scale.lower() == 'f':
            fahrenheit_converter(current_temp)

    if temp_scale.lower() == 'c':
            celsius_converter(current_temp)

# Function to convert from Celsius to Fahrenheit
def fahrenheit_converter(current_temp):
    degrees_fahrenheit = current_temp * 1.8 + 32
    print(f"\nThe current temperature in degrees Fahrenheit is: {degrees_fahrenheit:.1f}F.")

# Function to convert from Fahrenheit to Celsius
def celsius_converter(current_temp):
    degrees_celsius = (current_temp -32) / 1.8
    print(f"\nThe current temperature in degrees Celsius is: {degrees_celsius:.1f}C.")

main ()