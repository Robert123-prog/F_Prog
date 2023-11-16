class Statistics:
    def __init__(self, autos):
        self.autos = autos

    def anz(self, farbe):
        count = 0

        for auto in self.autos:
            if auto.farbe == farbe:
                count += 1

        return count

    def bauj(self, marke):
        s = 0
        count = 0

        for m in self.autos:
            if m.marke == marke:
                s += m.baujahr
                count += 1


        return s // count

