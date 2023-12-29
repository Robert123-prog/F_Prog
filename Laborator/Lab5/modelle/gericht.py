from abc import ABC, abstractmethod
from modelle.identifizierbar import Identifizierbar
class Dish(Identifizierbar):

    @abstractmethod
    def __init__(self, price: int, id: int, portion_size = 350):
        super().__init__(id)
        self.price = price
        self.portion_size = portion_size


