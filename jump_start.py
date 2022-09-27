# https://jump.hackjunction.com/challenges/4VMopGyMI5693GtY2pXvDg

def jump_start(n):
    if n % 15 == 0:
        return "JumpStart"
    if n % 5 == 0:
        return "Start"
    if n % 3 == 0:
        return "Jump"

    return n


if __name__ == "__main__":
    for i in range(100):
        print(jump_start(i))
