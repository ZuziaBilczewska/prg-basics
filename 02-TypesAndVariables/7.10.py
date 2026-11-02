###
# A program that enables a user to guess
# the number rolled by the computer.
#

import random

# Rzut komputera
computer = random.randint(1, 6)

# Twój typ
you = int(input("Guess the number from 1 to 6: "))

you_won = you == computer

print(f"Computer rolled: {computer}")
print(f"You won: {you_won}")