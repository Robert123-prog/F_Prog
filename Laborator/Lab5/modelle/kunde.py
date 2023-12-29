from modelle.identifizierbar import Identifizierbar

class Customer(Identifizierbar):

    def __init__(self, name: str, adresse: str, id: int):
        super().__init__(id)
        self.name = name
        self.adresse = adresse

    def __repr__(self):
        return f'Customer: ID = {self.id}, Name = {self.name}, Address = {self.adresse}'
