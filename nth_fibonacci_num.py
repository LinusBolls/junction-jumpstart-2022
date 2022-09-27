# https://jump.hackjunction.com/challenges/66PwviVKNWklmna4U6Yuur

def nth_fibonacci_num(n):

    if n < 3:
        return 1

    return nth_fibonacci_num(n - 1) + nth_fibonacci_num(n - 2)


if __name__ == "__main__":
    for i in range(11):
        print(i, nth_fibonacci_num(i))
