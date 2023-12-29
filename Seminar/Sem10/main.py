def prim(n):
    if n <= 1:
        return False

    for d in range(2, n // 2 + 1):

        if n % d == 0:
            return False

    return True

def gen(n, w):

    m = [[w for _ in range(n)] for _ in range(n)]
    p = [i for i in range(n * 20) if prim(i)]
    ct = 0

    for i in range(n):
        for j in range(n):

            if i > j:
                m[i][j] = p[0]
                p.pop(0)

            if i < j:
                m[i][j] = ct
                ct += 2

    return m

m = gen(5, 7)
#
# for line in m:
#     print(line)

def do_stuff(a, x, n):
    i = 0

    while (i <= n - 1 and a[i] != x):
        i += 1

    return i if i <= n else -1

def test_falsch():
    assert do_stuff([1, 2, 3, 4], 6, 4) == 2

def test_wahr():
    assert do_stuff([1, 2, 3, 4], 3, 4) == 2

#test_falsch()
#test_wahr()

def read(filename):
    f = open(filename, 'r')
    l = []

    for line in f:
        numbers = [int(num) for num in line.strip().split(',')]

        if not prim(sum(numbers)):
            return False

        l1 = [num for num in numbers if num % 2 == 0]
        l2 = [num for num in numbers if num % 2 != 0]

        if sorted(l1) != l1:
            return False

        if sorted(l2, reverse = True) != l2:
            return False

        l.append(numbers)

    if len(l[-1]) != 1:
        return False

    return True


