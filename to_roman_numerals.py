# https://jump.hackjunction.com/challenges/52f8Lx93X8c0Mltn6X3FrX

def to_roman_numerals(n):
    arabic_nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_nums = ["I", "IV", "V", "IX", "X", "XL",
                  "L", "XC", "C", "CD", "D", "CM", "M"]

    conversion_factor = 12

    str = ""

    while n:
        division = n // arabic_nums[conversion_factor]
        n %= arabic_nums[conversion_factor]

        while division:
            str += roman_nums[conversion_factor]
            division -= 1
        conversion_factor -= 1

    return str


if __name__ == "__main__":
    for i in range(100):
        print(to_roman_numerals(i))
