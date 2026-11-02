###
# A program that calculates the number of characters
# in a name, surname and full name.
#

name = "Anna"
surname = "May"

characters_in_name = len(name)
characters_in_surname = len(surname)
full_name = name + " " + surname
characters_in_full_name = len(full_name)

print(f"Your name has {characters_in_name} characters")
print(f"Your surname has {characters_in_surname} characters")
print(f"Your full name has {characters_in_full_name} characters")