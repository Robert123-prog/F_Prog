import math

class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __sub__(self, other):
    #     return Punkt(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return  Punkt(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f'X = {self.x}, Y = {self.y}'

class Kreis:
    def __init__(self, c : Punkt, r : int):
        self.c = c
        self.r = r

    def __str__(self):
        return f' C = ({self.c}), R = {self.r}'

    def move(self, delta):
        self.c.x += delta

    def __add__(self, other):
        return Kreis(self.c + other.c, self.r * other.r)

def main():
    p1 = Punkt(1, 2)
    p2 = Punkt(3, 5)
    p3 = p1 - p2
    # print(p3)

    k1 = Kreis(p1, 4)
    k2 = Kreis(Punkt(100, 2), 3)

    while k1.c - k2.c > k1.r + k2.r:
        k1.move(1)


    print(k1)
    print(k1 + k2)

main()
