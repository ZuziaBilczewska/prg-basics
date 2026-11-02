###
# A program that calculates the distance to the horizon.
#

import math

height = float(input("Enter height in meters: "))

distance = 3.57 * math.sqrt(height)

print("Distance to the horizon:", round(distance, 2), "km")