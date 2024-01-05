# from controller.controller import Controller
# from modelle.getrank import Drink
# from modelle.gekochtes_gericht import Cooked_Dish
# from repository.getrank_repo import DrinkRepo
# from repository.gekochtes_gericht_repo import CookedDishRepo
# from modelle.bestellung import Order
# from repository.bestellung_repo import OrderRepo
# from modelle.kunde import Customer
# from repository.kunde_repo import CustomerRepo
from ui.menu import UI

def main():

   # dr1 = Drink(1, 30, 20)
   # dr2 = Drink(2, 50, 30)
   #
   # c1 = Customer(1, 'David', 'Lazaret')
   # c2 = Customer(2, 'Robert', 'Livezii')
   #
   # repo_cust = CustomerRepo()
   # repo_cust.add_customers(c1)
   # repo_cust.add_customers(c2)
   # repo_cust.save()
   #
   # d1 = Cooked_Dish(1, 100, 12)
   # d2 = Cooked_Dish(2, 200, 22)
   #
   #
   #
   # cont = Controller()
   #
   # repo_drinks = DrinkRepo()
   # repo_dishes = CookedDishRepo()
   #
   # repo_dishes.add_cookedDishes(d1)
   # repo_dishes.add_cookedDishes(d2)
   # repo_dishes.save()
   #
   # repo_drinks.add_drinks(dr1)
   # repo_drinks.add_drinks(dr2)
   # repo_drinks.save()
   #
   #
   # o1 = Order(1, 1, [1], [1, 2])
   # o2 = Order(2, 2, [1, 2], [1, 2])
   # repo_orders = OrderRepo()
   #
   # orders = repo_orders.load_to_list()
   #
   # print(orders)
   #print(o1.calc_cost(repo_dishes, repo_drinks))

   #print(o1.show_bill(repo_dishes, repo_drinks))

   '''
   vezi UI
   vezi metode write si convert
   total cost din controller nu merge pt ceva motiv
   n am testat tot, dar merge chiar ok, vezi search dupa partial name
   
   '''

   menu = UI()
   menu.run_2_0()



main()

