from ex5.kreis import Kreis
from ex5.dreieck import Dreieck
from ex5.test import test_flache

def main():
    k = Kreis(4)
    print(k.k_fl())

    d = Dreieck(4, 5)
    print(d.d_flache())

test_flache()
main()