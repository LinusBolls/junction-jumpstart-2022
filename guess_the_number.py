# https://jump.hackjunction.com/challenges/36wMLCtNv42h4tRoOjrD0L

from random import randint


def main():

    min = 1
    max = 10

    player_choice = input(f"(number from {min} - {max}) > ")

    num = randint(min, max)

    if player_choice == num:
        print("congratulations!")
    else:
        print(f"bad luck, the number was {num}")

    main()


if __name__ == "__main__":
    main()
