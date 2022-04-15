from q1 import ascii_to_string
from q2 import permutate
from q3 import get_smallest_pair, smallest_sum


def test_q1():
    # =======================================
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


def test_q2():
    # =======================================
    assert (permutate("r2d2c3pxxx")) == 0
    assert (permutate("c3por2d2")) == 2
    assert (permutate("22a3xcpordd")) == 20
    assert (permutate("223xcpord")) == 6
    assert (permutate("22a3xcpord")) == 12


def test_q3():
    # =======================================
    assert get_smallest_pair([1, 2, 3, 4]) == [1, 2]
    assert get_smallest_pair([-1, -2, -3, 4]) == [-3, -2]
    assert get_smallest_pair([0, 4, 1, 2]) == [0, 1]
    assert get_smallest_pair([0, 0, 1, 4]) == [0, 0]
    assert get_smallest_pair([4, 1, 0, 0]) == [0, 0]
    assert smallest_sum(15, 5, [12, 2, 5, 14, 1]) == 4
    assert smallest_sum(6, 3, [1, 2, 3]) == 3
    assert smallest_sum(-20, 6, [25, 15, 5, -5, -15, -25]) == 5
    assert smallest_sum(100, 3, [33, 34, 35]) == 0
