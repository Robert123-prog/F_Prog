# func

def cmmdc(nr1, nr2):
    while nr1 != nr2:
        if nr1 > nr2:
            nr1 -= nr2
        else:
            nr2 -= nr1

    return nr1

n = int(input("n = "))
num = 2

if (n <= 1) :
    print(0)

while num < n :

    if cmmdc(n, num) == 1 :
        print(num, " ")
        num += 1

    else :
        num += 1