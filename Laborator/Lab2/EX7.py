'''
Functiile "cmmmc" si "cmmdc" calculeaza cmmmc respectiv cmmdc a 2 nr oarecare

Functia "cmmmc_vect" calculeaza cmmmc-ul elementelor dintr-un vector oarecare, dintre pozitia fr si to

'''


def cmmmc(nr1, nr2):
    p = nr1 * nr2

    cmmmc = p // cmmdc_numar(nr1, nr2)

    return cmmmc


def cmmdc_numar(nr1, nr2):

    while nr1 != nr2:

        if nr1 > nr2:

            nr1 -= nr2

        else:

            nr2 -= nr1

    return nr1
def cmmmc_vect(vect, fr, to):

    cmmmc_fin = cmmmc(vect[fr], vect[fr + 1])

    for i in range(fr + 2, to + 1, 1):

        cmmmc_fin = cmmmc(cmmmc_fin, vect[i])

    return cmmmc_fin

# def cmmdc_vect(vect):
#
#     cmmdc = cmmdc_numar(vect[0], vect[1])
#
#     for i in range(2, len(vect), 1):
#         cmmdc = cmmdc_numar(cmmdc, vect[i])
#
#     return cmmdc

# def cmmmc(vect, fr, to):
#     prod = 1
#
#     for i in range(fr, to, 1):
#         prod *= i
#
#     cmmmc = prod // cmmdc_vect(vect)
#
#     return cmmmc

def main():
    print(cmmmc_vect([12, 24, 48,8, 16, 12, 20, 30], 0, 2))

main()