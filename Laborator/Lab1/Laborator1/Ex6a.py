
def count_zero(p):
    ct = 0

    while p % 10 == 0:
        ct += 1
        p /= 10

    return ct

n = int(input("n = "))
prod = 1

while n != 0:
    prod *= n
    n = int(input("n = "))

print(prod, '\n')

print(count_zero(prod))

