from ex4.test import test_konto
from ex4.konto import Konto

def main():
    k = Konto('09absd', 100)
    
    k.einzahlen(100)
    print(k.betrag)

    k.auszahlen(50)
    print(k.betrag)

test_konto()
main()