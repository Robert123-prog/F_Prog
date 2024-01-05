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


    def add_customer(self, customer_id, customer_name, customer_address):
        customer = Customer(customer_id, customer_name, customer_address)
        self.customer_repo.add_customers(customer)
        self.customer_repo.save()

    def add_drink(self, id, price, alc_content):
        drink = Drink(id, price, alc_content)
        self.drink_repo.add_drinks(drink)
        self.drink_repo.save()

    def add_cooked_dish(self, id, price, prep_time, portion_size):
        dish = Cooked_Dish(id, price, prep_time, portion_size)
        self.cookedDish_repo.add_cookedDishes(dish)
        self.cookedDish_repo.save()

    def add_order(self, id, customer_id, list_of_dish_id, list_of_drink_id):
        order = Order(id, customer_id, list_of_dish_id, list_of_drink_id)
        self.order_repo.add_orders(order)
        self.order_repo.save()

    def show_total_cost(self, order: Order):
        print(order.calc_cost(self.cookedDish_repo, self.drink_repo))


    '''
    show_total_cost2 se bazeaza doar pe id-ul fiecarei comezi
    NEFUNCTIONALA
    '''

    # def show_total_cost2(self, id_of_order):
    #     orders = self.order_repo.load_to_list()
    #
    #     for order in orders:
    #         if order.id == id_of_order:
    #             return self.order.calc_cost(self.cookedDish_repo, self.drink_repo)
    #
    # def show_bill(self, order: Order):
    #     return order.show_bill(self.cookedDish_repo, self.drink_repo)

    def search_for_customer(self, cust_partial_name):
        return self.customer_repo.search_after_partial_name_filt2(cust_partial_name)

    def search_for_customer_after_part_address(self, cust_partial_address):
        return self.customer_repo.search_after_partial_address_with_filter(cust_partial_address)

    def update_customers_name(self, old_name: str, new_name: str):
        self.customer_repo.update_cust_name(old_name, new_name)

    def print_customers(self):
        print(self.customer_repo.load_to_list())

    def return_all_customers(self):
        return self.customer_repo.load_to_list()

    def return_all_drinks(self):
        return self.drink_repo.load_to_list()

    def return_all_cooked_dishes(self):
        return self.cookedDish_repo.load_to_list()

    def return_all_orders(self):
        return self.order_repo.load_to_list()

    def print_drinks(self):
        print(self.drink_repo.load_to_list())

    def print_cooked_dishes(self):
        print(self.cookedDish_repo.load_to_list())

    def print_orders(self):
        print(self.order_repo.load_to_list())