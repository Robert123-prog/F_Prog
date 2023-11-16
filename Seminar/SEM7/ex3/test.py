from ex3.auto import Auto
from ex3.stats import Statistics

def test_farbe():
    autos = [Auto('dacia', 'sandero', 2010, 'grau'),
             Auto('dacia', '1310', 1970, 'rot'),
             Auto('ferrari', 'enzo', 2009, 'rot')]

    s = Statistics(autos)

    assert s.anz('rot') == 2

def test_avg():
    autos = [Auto('dacia', 'sandero', 2010, 'grau'),
             Auto('dacia', '1310', 1970, 'rot'),
             Auto('ferrari', 'enzo', 2009, 'rot')]

    s = Statistics(autos)

    assert s.bauj('dacia') == 1990

