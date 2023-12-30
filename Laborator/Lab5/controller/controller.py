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

    def add_drink(self, id, price, alc_content):
        drink = Drink(id, price, alc_content)
        return self.drink_repo.add_drinks(drink)

    def add_cooked_dish(self, id, price, prep_time, portion_size):
        dish = Cooked_Dish(id, price, prep_time)
        return self.cookedDish_repo.add_cookedDishes(dish)

    def add_order(self, id, customer_id, list_of_dish_id, list_of_drink_id):
        order = Order(id, customer_id, list_of_dish_id, list_of_drink_id)
        return self.order_repo.add_orders(order)

    def show_total_cost(self, order: Order):
        return order.calc_cost(self.cookedDish_repo, self.drink_repo)

    def show_bill(self, order: Order):
        return order.show_bill(self.cookedDish_repo, self.drink_repo)


