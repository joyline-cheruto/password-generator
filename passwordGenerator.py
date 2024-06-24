import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_?"
password = ""
for x in range(16):
    password += random.choice(chars)

print(f"Your Password is: {password}")
