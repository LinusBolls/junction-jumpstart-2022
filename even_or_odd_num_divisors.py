# https://jump.hackjunction.com/challenges/5IOD2REbenD7GRHE9VkJi1

def even_or_odd_num_divisors(num):
    divisors = []

    for i in range(1, num + 1):

        if num % i == 0:
            divisors.append(i)

    has_even_num_divisors = len(divisors) % 2 == 0

    return "even" if has_even_num_divisors else "odd"


if __name__ == "__main__":
    for i in range(100):
        print(even_or_odd_num_divisors(i))
