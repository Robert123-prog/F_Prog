from ex2.test import test_red
from ex2.bruch import Bruch
def main():
    b = Bruch(14, 22)
    b.erw(3)
    print(b.n, b.m)

test_red()
main()