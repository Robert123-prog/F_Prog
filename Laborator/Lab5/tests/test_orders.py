'''
Test the functionality for orders
'''

from modelle.bestellung import Order
from repository.bestellung_repo import OrderRepo
from modelle.kunde import Customer
from repository.kunde_repo import CustomerRepo
from modelle.getrank import Drink
from repository.getrank_repo import DrinkRepo
from modelle.gekochtes_gericht import Cooked_Dish
from repository.gekochtes_gericht_repo import CookedDishRepo

o1 = Order(1, 1, [1, 2], [1, 2])
o2 = Order(2, 1, [1], [2])

c1 = Customer(1, 'David', 'Lazaret')
c2 = Customer(2, 'Robert', 'Livezii')

dr1 = Drink(1, 30, 15)
dr2 = Drink(2, 50, 30)

d1 = Cooked_Dish(1, 100, 15)
d2 = Cooked_Dish(2, 200, 30)

repo_orders = OrderRepo()
repo_dishes = CookedDishRepo()
repo_drinks = DrinkRepo()
repo_customers = CustomerRepo()

repo_dishes.add_cookedDishes(d1)
repo_dishes.add_cookedDishes(d2)
repo_dishes.save()

repo_drinks.add_drinks(dr1)
repo_drinks.add_drinks(dr2)
repo_drinks.save()

repo_customers.add_customers(c1)
repo_customers.add_customers(c2)
repo_customers.save()

repo_orders.add_orders(o1)
repo_orders.add_orders(o2)
repo_orders.save()

def test_bill():

    dishes = o1.bill(repo_dishes, repo_drinks)[0]
    drinks = o2.bill(repo_dishes, repo_drinks)[1]

    #assert len(dishes) == 0 and len(drinks) == 0 #Error
    assert len(dishes) != 0 and len(drinks) != 0

#test_bill()

def test_save_order_to_file():

    repo_orders.add_orders(o1)
    repo_orders.add_orders(o2)
    repo_orders.save()

    #assert not repo_orders.filename #Error
    assert repo_orders.filename

test_save_order_to_file()

def test_order_from_file():

    repo_orders.add_orders(o1)
    repo_orders.add_orders(o2)
    repo_orders.save()


    orders = repo_orders.load_to_list()

    #assert len(orders) == 0 #Error
    assert len(orders) != 0

test_order_from_file()


