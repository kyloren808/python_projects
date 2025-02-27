import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojii = {ROCK: "🪨", SCISSORS: "✂️", PAPER: "📄"}
choices = tuple(emojii.keys())


def check_for_winner(u_choice, c_choice):
    if (
        (u_choice == ROCK and c_choice == SCISSORS)
        or (u_choice == PAPER and c_choice == ROCK)
        or (u_choice == SCISSORS and c_choice == PAPER)
    ):
        print("You win!")
    elif (u_choice == PAPER and c_choice == SCISSORS) or (
        u_choice == SCISSORS and c_choice == ROCK
    ):
        print("You lose!")
    else:
        print("Draw!")


def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissors? r/p/s: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(u_choice, c_choice):
    print(f"You chose {emojii[u_choice]}")
    print(f"Computer chose {emojii[c_choice]}")


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        check_for_winner(user_choice, computer_choice)

        continue_game = input("Continue? (y/n): ").lower()
        if continue_game == "n":
            print("Thanks for playing.")
            break
        else:
            continue


play_game()
