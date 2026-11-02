###
# A program that prints the numerical representation
# of each letter of a name.
#

name = "John"

for letter in name:
    print(f"The letter {letter} has a code {ord(letter)}")