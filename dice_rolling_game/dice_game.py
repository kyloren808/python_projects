# Dice Rolling Game
import random

while True:
    user_input = input("Roll the dice? (y/n): ").lower()
    if user_input == "y":
        die_one = random.randint(1, 6)
        die_two = random.randint(1, 6)
        print(f"({die_one}, {die_two})")
    elif user_input == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
