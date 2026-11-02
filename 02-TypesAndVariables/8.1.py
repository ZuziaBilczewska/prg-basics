###
# Calculation of circle area and circumference.
#

import math

r = float(input("Enter radius: "))

circumference = 2 * math.pi * r
area = math.pi * r ** 2

print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")