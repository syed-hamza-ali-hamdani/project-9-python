# Password Generator python project -7

import random
import string

# Introduction
print("Welcome to the Password Generator!")
print("Generate a strong, random password easily.\n")

try:
    password_length = int(input("Enter the desired password length (minimum 6 characters): "))
    if password_length < 6:
        print("Password length must be at least 6 characters.")
        exit()
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Characters to include in the password
letters = string.ascii_letters  
digits = string.digits 
symbols = string.punctuation 

all_characters = letters + digits + symbols

# Generate random password
password = "".join(random.choice(all_characters) for _ in range(password_length))

# Display the generated password
print(f"\nYour random password is: {password}")
print("Keep it safe!")