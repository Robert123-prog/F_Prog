class Konto:
    def __init__(self, nummer, betrag = 0):
        self.nummer = nummer
        self.betrag = betrag
        self.admin = None

    def einzahlen(self, b):
        self.betrag += b

    def auszahlen(self, b):
        self.betrag -= b

    def set_admin(self, admin):
        self.admin = admin