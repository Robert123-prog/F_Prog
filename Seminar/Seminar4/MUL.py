'''
Documentatie
'''



from math import gcd

def mul(a, b):
    return simplify((a[0] * b[0], a[1] * b[1]))

def simplify(a):
    d = gcd(a[0], a[1])

    return a[0] // d, a[1] // d


def add_frac(fracs, frac):
    fracs.append(frac)

def mul_fracs(fracs):
    p = 1, 1

    for frac in fracs:
        p = mul(p, frac)

    return p
def menu():
    return """
        1 - add frac
        2 - mul fracs
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
            p = mul_fracs(fracs)
            print('prod = ', p)

        if opt == 0:
            break

main()



