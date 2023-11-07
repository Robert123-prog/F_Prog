"""
Documentatie
"""


def calc_max(vect):
    mx = 0

    for i in vect:

        if i >= mx:

            mx = i

    return mx

def test_calc_max():
    assert calc_max([1, 2, 5, 9, 10, 11, 3, 4]) == 11

def calc_min(vect):
    mn = 99999999999

    for i in vect:

        if i <= mn:

            mn = i

    return mn

def test_calc_min():
    assert calc_min([1, 2, 5, 9, 10, 11, 3, 4]) == 1

def main():
    l = [1, 2, 5, 9, 10, 11, 3, 4]

    print(calc_min(l), " ",calc_max(l))

main()
