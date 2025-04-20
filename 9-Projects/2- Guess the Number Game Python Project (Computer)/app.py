# Guess the Number Game - Computer Guesses -2

import random

#Introduction
print("Wellcome to the guess the Number Game!")
print("Think of a number Between 1 and 100, and i will try to guess it.")
print("You can tell me if my guess is too high (H), too low (L), or correct (C).")


# Initial range for guessing

low = 1
high = 100
guesses = 0

while True:
    # Computer Guesses a number
    guess = random.randint(low, high)
    guesses += 1

    #show the computer's guess 
    print(f"My guess is: {guess}")
    user_input = input("Is my guess too high (H), too low  (L), or correct (C)? ").upper()

    # check user response 
    if user_input == 'H':
        high = guess - 1 
    elif user_input == 'L':
        low = guess + 1
    elif user_input == 'C':
        print(f"Yay | I guessed your number is {guesses} tries|")
        break
    else:
        print("Invalid Input. Please enter H, L, or C.")
