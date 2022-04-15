import string


def ascii_to_string(ascii: string) -> string:
    """
    :param ascii: ascii string itself.
    :return: human readable string.
    """
    i = 0
    current_string = ""
    while i <= len(ascii) - 2:
        if (int(ascii[i:i + 2])) >= 32:
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


if __name__ == '__main__':
    assert ascii_to_string('1221019811497') == "zebra"
    assert ascii_to_string('1145010050') == "r2d2"
    assert ascii_to_string(
        '701051141151164432115111108118101321161041013211211411198108101109463284104101110443211911410511610132116104101329911110010146') == "First, solve the problem. Then, write the code."
    assert ascii_to_string(
        '8211798121321051153211411798981051151043332807280321051153211210411297110116971151161059933') == "Ruby is rubbish! PHP is phpantastic!"
    assert ascii_to_string(
        '66101102111114101321151111021161199711410132999711032981013211410111711597981081013210511632102105114115116321049711532116111329810132117115979810810146') == "Before software can be reusable it first has to be usable."
    assert ascii_to_string(
        '6711110010132105115321081051071013210411710911111446328710410111032121111117321049711810132116111321011201121089710511032105116443210511639115329897100') == "Code is like humor. When you have to explain it, it's bad"