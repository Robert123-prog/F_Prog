class Bruch:

    def __init__(self, n, m):
        self.n = n
        self.m = m

    def erw(self, k):
        self.n *= k

    def kurz(self, k):
        self.m //= k
        self.n //= k

    def red(self):
        k = self.gcd()

        self.kurz(k)

    def gcd(self):
        a = self.n
        b = self.m

        while a != b:

            if a < b:
               b -= a

            else:
                a -= b

        return a