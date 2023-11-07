'''
Documentatie
'''

(2, 3) , (5, 6)

from math import gcd

def div(a, b):
    return simplify((a[0] * b[1], a[1] * b[0]))

def simplify(a):
    d = gcd(a[0], a[1])

    return a[0] // d, a[1] // d


def add_frac(fracs, frac):
    fracs.append(frac)

def div_fracs(fracs):
    p = fracs[0]

    for frac in fracs:
        p = div(p, frac)

    return p
def menu():
    return """
        1 - add frac
        2 - div fracs
        0 - exit
    """

def main():
    fracs = []

    while True:
        print(menu())
        opt = int(input('opt = '))

        if opt == 1:
            n = int(input('n = '))
            m = int(input('m = '))

            add_frac(fracs, (n, m))

        if opt == 2:
            p = div_fracs(fracs)
            print('div = ', p)

        if opt == 0:
            break

main()


