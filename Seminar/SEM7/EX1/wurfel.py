import random

class Wurfel:
    def __init__(self, augen):
        self.augen = augen

    def werfen(self):
     return random.randint(1, self.augen)

