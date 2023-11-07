#ex: n = 11, a[i] = 2 1 5 2 3 8 2 1 6 5 2
# 6B


def is_prim(nr):

    if nr <= 1:
        return False
    else:
        for d in range(2, nr // 2 + 1, 1):
            if nr % d == 0:
                return False

    return True


a = [0] * 100
lg = 1
lgmax = 1
n = int(input("n = "))

for i in range(1, n + 1):
    a[i] = int(input("element = "))

for i in range(1, n):
    s = a[i] + a[i + 1]

    if is_prim(s) == True:
        lg += 1

    else:
        lg = 1

    if lg > lgmax:
        lgmax = lg


print(lgmax)


