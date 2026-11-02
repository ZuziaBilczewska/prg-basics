###
# A program that calculates the population
# of the Northern and Southern Hemispheres.
#

total = 8000000000
north = 7200000000

south = total - north

north_percentage = north / total * 100
south_percentage = south / total * 100

print("World population:", total)
print("Northern Hemisphere:", north)
print("Northern Hemisphere in %:", north_percentage)

print("Southern Hemisphere:", south)
print("Southern Hemisphere in %:", south_percentage)