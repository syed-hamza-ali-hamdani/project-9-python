# Guess the Number Game - User Guesses -3

import random

# Introduction
print("Welcome to the Guess the Number Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Generate Random Number
number = random.randint(1, 100)
guesses = 0

while True:
    # User se input lena
    user_guess = input("Enter your guess: ")

    # Input ko integer mein convert karna
    try:
        user_guess = int(user_guess)
        guesses += 1

        # Guess ko check karna
        if user_guess < number:
            print("Too low! Try again.")
        elif user_guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            break 
    except ValueError:
        print("Please enter a valid number.")