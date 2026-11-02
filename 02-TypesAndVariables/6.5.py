###
# A program that formats a 9-digit phone number.
#

phone = input("Enter phone number: ")

print(f"Phone number: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}")