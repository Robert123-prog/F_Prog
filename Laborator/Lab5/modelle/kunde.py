from identifizierbar import Identifizierbar

class Customer(Identifizierbar):

    def __init__(self, name: str, adresse: str, id: int):
        super().__init__(id)
        self.name = name
        self.adresse = adresse


