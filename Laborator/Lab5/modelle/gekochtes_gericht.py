from modelle.gericht import Dish

class Cooked_Dish(Dish):
    def __init__(self, id, price, preparation_time, portion_size = 350):
        super().__init__(price, id, portion_size)
        self.preparation_time = preparation_time



