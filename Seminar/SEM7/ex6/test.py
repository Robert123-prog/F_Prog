from ex6.zahler import Zahler

def test_counter():
    c = Zahler(0)

    assert c.cnt() == 10

