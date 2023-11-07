#func

#ex: n = 6, a[i] = 3 10 1 2 4 8
def cmmdc(nr1, nr2):
    while nr1 != nr2:
        if nr1 > nr2:
            nr1 -= nr2
        else:
            nr2 -= nr1

    return nr1

def main():
    n = int(input("n = "))
    a = [0] * 100

    for i in range(0, n, 1):
        a[i] = int(input("element = "))

    lg = 1
    lgmx = 1

    for i in range(1, n):
        if cmmdc(a[i], a[i + 1]) == 1:
            lg += 1
        else:
            lg = 1

        if lg > lgmx:
            lgmx = lg

    print(lgmx)

main()
