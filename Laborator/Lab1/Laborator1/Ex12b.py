#func

a = [0] * 100
n = int(input("n ="))

for i in range(1, n + 1):
    a[i] = int(input("a[i] = "))

lg = 1
lgmax = 1
s = 0
smax = 0

for i in range(n + 1):
    s = a[i] + a[i + 1]

    if s > smax:
        smax = s
        lg += 1

    if lg > lgmax:
        lgmax = lg

print(lgmax)

