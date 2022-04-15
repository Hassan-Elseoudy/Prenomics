import string
from collections import defaultdict


def permutate(input: string) -> int:
    count = {'c': -1, '3': -1, 'p': -1, 'o': -1, 'r': -1, 'd': -1, '2': -1}
    for i in input:
        count[i] = count.get(i, 0) + 1

    if any(v < 1 for v in count.values()):  # Can't construct
        return 0


    return ""


if __name__ == '__main__':
    print(permutate("c3por2d2"))
    