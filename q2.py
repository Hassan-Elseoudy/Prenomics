import string


class UniqueElement:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences


def perm_unique(elements):
    eset = set(elements)
    listunique = [UniqueElement(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)


def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in perm_unique_helper(listunique, result_list, d - 1):
                    yield g
                i.occurrences += 1


def permutate(input: string) -> int:
    count = {'c': -1, '3': -1, 'p': -1, 'o': -1, 'r': -1, 'd': -1, '2': -2}
    for i in input:
        count[i] = count.get(i, 0) + 1

    if any(v < 0 for v in count.values()):  # Can't construct
        return 0

    required_list = list(dict(filter(lambda item: item[1] > 0, count.items())).values()) + ["c3po", "r2d2"]

    return len(list(perm_unique(required_list)))


if __name__ == '__main__':
    assert (permutate("r2d2c3pxxx")) == 0
    assert (permutate("c3por2d2")) == 2
    assert (permutate("22a3xcpordd")) == 20
    assert (permutate("223xcpord")) == 6
    assert (permutate("22a3xcpord")) == 12

    """
    Referenced from: https://stackoverflow.com/a/6285203
    """