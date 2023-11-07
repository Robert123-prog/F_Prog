
def check_prime(nr):
    for d in range(2, nr // 2 + 1):
        if nr % d == 0:
            return False

    return True

n = int(input("n = "))
pr = 2

while n > 0:

    if check_prime(pr) == True:
        print(pr, " ")
        n -= 1
        pr += 1

    else:
        while check_prime(pr) != True:
            pr += 1

