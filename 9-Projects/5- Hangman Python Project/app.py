# Hangman Game Python Project -5
import random

# Words list
words = ["python", "programming", "hangman", "development", "computer"]

# Choose a random word
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)  
attempts = 6 
guessed_letters = [] 

# Introduction
print("Welcome to the Hangman Game!")
print("Guess the secret word letter by letter.")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chances. Good luck!\n")

while attempts > 0:
    # Display current progress
    print("Word:", " ".join(guessed_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

    # User input
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.\n")
        continue

    # Check if the letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter! Try again.\n")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        print(f"Good job! {guess} is in the word.\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print(f"Oops! {guess} is not in the word.\n")
        attempts -= 1

    # Check if the user has guessed the word
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

# If the user runs out of attempts
if attempts == 0:
    print("Game Over! You ran out of attempts.")
    print(f"The secret word was: {secret_word}")