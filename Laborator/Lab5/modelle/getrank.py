from modelle.gericht import Dish

class Drink(Dish):
    def __init__(self, price, id, alc_content):
        super().__init__(price, id)
        self.alc_content = alc_content
        self.drinks = []

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def save_to_file(self):
        pass
