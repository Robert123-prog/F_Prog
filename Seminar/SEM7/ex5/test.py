import math

from ex5.kreis import Kreis
from ex5.dreieck import Dreieck

def test_flache():
    k = Kreis(4)
    assert k.k_fl() == math.pi * 16

    d = Dreieck(4, 5)

    assert d.d_flache() == 10


