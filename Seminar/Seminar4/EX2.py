from math import gcd

'''
1. de implementat sub, mul, div
2. metod pt stergere din lista
3. calcul min/max din lista
4. optiuni pentru stergere si min/max (meniu)
'''


def simplify(a):
    d = gcd(a[0], a[1])

    return a[0] // d, a[1] // d

def sub(a, b):
    return simplify((a[0] * b[1] - a[1] * b[0], a[1] * b[1]))

def add_frac(fracs, frac):
    fracs.append(frac)

def sub_frac(fracs):
    s = fracs[0]

    for frac in fracs:
            s = sub(s, frac)

    return s

def menu():
    return """
        1 - add frac
        2 - sub fracs
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
            s = sub_frac(fracs)
            print('sum = ', s)

        if opt == 0:
            break

main()
