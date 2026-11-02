###
# A program that calculates the volume
# and surface area of a cuboid.
#

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)

print(f"The volume of the cuboid is {volume}")
print(f"The surface area of the cuboid is {surface_area}")