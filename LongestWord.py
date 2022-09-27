# https://jump.hackjunction.com/challenges/5SplFsXF7uNUbYySc43kKt

def LongestWord(sen):
    words = sen.split(" ")

    words.sort(key=lambda word: len(word), reverse=True)

    return words[0]


if __name__ == "__main__":
    print(LongestWord("moin meister die sache"))

    print(LongestWord("riesengroßes wort"))

    print(LongestWord("anbei"))

    print(LongestWord(""))
