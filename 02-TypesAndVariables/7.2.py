###
# A program that checks whether the password
# has at least 8 characters.
#

password = input("Enter password: ")

password_ok = len(password) >= 8

print(f"Password length is valid: {password_ok}")