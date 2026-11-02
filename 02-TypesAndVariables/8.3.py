###
# A program that converts height from centimeters
# to feet and inches.
#

cm = 170

total_inches = int(cm / 2.54)

feet = total_inches // 12
inches = total_inches % 12

print(f"I am {cm} cm tall, i.e. {feet} feet and {inches} inches")