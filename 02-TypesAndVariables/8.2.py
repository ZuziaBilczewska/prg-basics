###
# A program that converts Celsius temperature
# to Kelvin and Fahrenheit.
#

celsius = float(input("Enter temperature in Celsius: "))

kelvin = celsius + 273.15
fahrenheit = celsius * 9 / 5 + 32

print(f"Temperature in Kelvin: {kelvin:.2f} K")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")