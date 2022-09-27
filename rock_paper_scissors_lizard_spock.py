# https://jump.hackjunction.com/challenges/7djMxuc25ctj9pP0q2seNzv

from random import choice

choices = ["rock", "paper", "scissors", "lizard", "spock"]

beaten_by = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["rock", "scissors"]
}


def get_outcome(player_choice, ai_choice):
    if player_choice in beaten_by[ai_choice]:
        return "the ai wins!"

    if ai_choice in beaten_by[player_choice]:
        return "you win!"

    return "it's a draw!"


def main():

    player_choice = ""

    while not player_choice in choices:
        player_choice = input("(" + " | ".join(choices) + ") > ")

        if not player_choice in choices:
            print("please choose a valid move")

    ai_choice = choice(choices)

    outcome = get_outcome(player_choice, ai_choice)

    print("the ai chose " + ai_choice)

    print(outcome)

    main()


if __name__ == "__main__":
    main()
