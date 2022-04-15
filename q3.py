import string


def get_smallest_two(numbers: []) -> list:
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return [m1, m2]


def smallest_sum(v: int, length: int, numbers: []) -> int:
    """
   :param v: not greater than
   :param length: size of input
   :param numbers: array of numbers
   :return: quantity of the given numbers that can be added up
   with other two of these numbers so that the result is not greater than v.

   We get the smallest 2 elements, and to try with other numbers.
   """
    smallest_two = get_smallest_two(numbers)
    smallest_two_sum = sum(smallest_two)
    numbers.remove(smallest_two[0])
    numbers.remove(smallest_two[1])
    elements = list(filter(lambda number: smallest_two_sum + number <= v, numbers))
    return len(elements)


if __name__ == '__main__':
    assert get_smallest_two([1, 2, 3, 4]) == [1, 2]
    assert get_smallest_two([-1, -2, -3, 4]) == [-3, -2]
    assert get_smallest_two([0, 4, 1, 2]) == [0, 1]
    assert get_smallest_two([0, 0, 1, 4]) == [0, 0]
    assert get_smallest_two([4, 1, 0, 0]) == [0, 0]

    assert smallest_sum(15, 5, [12, 2, 5, 14, 1]) == 4
    assert smallest_sum(6, 3, [1, 2, 3]) == 3
    assert smallest_sum(-20, 6, [25, 15, 5, -5, -15, -25]) == 5
    assert smallest_sum(100, 3, [33, 34, 35]) == 0

    v = int(input())
    size = int(input())
    numbers = list(map(int, input().split(" ")))
    print(smallest_sum(v, size, numbers))

