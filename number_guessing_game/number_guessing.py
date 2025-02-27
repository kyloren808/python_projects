# Number Guessing Game

from random import randint

guess = randint(1, 100)

while True:
    try:
        response = int(input("Guess the number between 1 and 100: "))

        if response == guess:
            print("Congratulations! You guessed the number.")
            break

        if response > guess:
            print("Too high!")

        if response < guess:
            print("Too low!")
    except ValueError:
        print("Please enter a valid number")
