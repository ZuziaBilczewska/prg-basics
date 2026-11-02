###
# A program that checks whether a tree can be cut down.
#

import math

circumference = float(input("Enter tree circumference in cm: "))

diameter = circumference / math.pi
can_be_cut = diameter >= 50

print(f"Tree diameter: {diameter:.2f} cm")
print(f"Tree can be cut down: {can_be_cut}")