from modelle.identifizierbar import Identifizierbar
from functools import reduce
from modelle.gekochtes_gericht import Cooked_Dish
from modelle.getrank import Drink

class Order(Identifizierbar):
    def __init__(self, id, customer_id, list_of_dish_id, list_of_drink_id, total_cost):
        super().__init__(id)
        self.customer_id = customer_id
        self.list_of_dish_id = list_of_dish_id
        self.list_of_drink_id = list_of_drink_id
        self.total_cost = total_cost

    def calc_cost(self):
        #cu reduce
        pass

    def bill(self):
        pass

    def show_bill(self):
        pass




