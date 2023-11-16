from ex2.bruch import Bruch

def test_red():
    b = Bruch(14, 22)

    b.red()

    assert b.n == 7
    assert b.m == 11

