from modelle.getrank import Drink
from modelle.gekochtes_gericht import Cooked_Dish
from modelle.kunde import Customer
from modelle.bestellung import Order
from repository.kunde_repo import CustomerRepo
from repository.getrank_repo import DrinkRepo
from repository.bestellung_repo import OrderRepo
from repository.gekochtes_gericht_repo import CookedDishRepo


class Controller:
    def __init__(self):
        self.drink_repo = DrinkRepo()
        self.customer_repo = CustomerRepo()
        self.order_repo = OrderRepo()
        self.cookedDish_repo = CookedDishRepo()

    def add_customer(self, customerName, customerAdress, customerID):
        customer = Customer(customerName, customerAdress, customerID)
        return self.customer_repo.add_customers(customer)
