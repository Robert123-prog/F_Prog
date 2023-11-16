from ex4.konto import Konto

def test_konto():
    k = Konto("abcd012")
    k.set_admin("Eu")

    k.einzahlen(100)

    assert k.betrag == 100
