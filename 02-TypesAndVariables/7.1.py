###
# A program that checks tax exemption based on age.
#

age = int(input("Enter age: "))

no_tax = age <= 26

print(f"Exemption from paying taxes: {no_tax}")