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