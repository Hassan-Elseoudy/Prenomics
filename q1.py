# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import string

possible_words = []


# 1145010050
def ascii_to_string(ascii: string) -> string:
    i = 0
    current_string = ""
    while i <= len(ascii) - 2:
        if (int(ascii[i:i + 2])) >= 32:  # Might work
            current_ascii = int(ascii[i:i + 2])
            if (int(ascii[i:i + 3])) <= 122:
                current_ascii = int(ascii[i:i + 3])
                current_string += chr(current_ascii)
                i += 3
            else:
                current_string += chr(current_ascii)
                i += 2
        else:
            current_ascii = int(ascii[i:i + 3])
            if current_ascii <= 122:
                current_string += chr(current_ascii)
                i += 3
            else:
                print("Invalid!")
                return
    return current_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert(ascii_to_string('1221019811497'), "zebra")
    assert (ascii_to_string('1145010050'), "zebra")
    assert (ascii_to_string('701051141151164432115111108118101321161041013211211411198108101109463284104101110443211911410511610132116104101329911110010146'), "zebra")
    assert (ascii_to_string('8211798121321051153211411798981051151043332807280321051153211210411297110116971151161059933'), "zebra")
    assert (ascii_to_string('66101102111114101321151111021161199711410132999711032981013211410111711597981081013210511632102105114115116321049711532116111329810132117115979810810146'), "zebra")
    assert (ascii_to_string('1221019811497'), "zebra")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
