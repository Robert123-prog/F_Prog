from modelle.bestellung import Order
from modelle.gekochtes_gericht import Cooked_Dish
from modelle.getrank import Drink
from repository.getrank_repo import DrinkRepo
from repository.gekochtes_gericht_repo import CookedDishRepo

def main():
    cd_repo = CookedDishRepo()
    dr_repo = DrinkRepo()
    d1 = Cooked_Dish(1, 100, 10)
    d2 = Cooked_Dish(2, 200, 20)
    d3 = Cooked_Dish(3, 100, 15)

    dr1 = Drink(1, 10, 15)
    dr2 = Drink(2, 30, 30)

    cd_repo.add_cookedDishes(d1)
    cd_repo.add_cookedDishes(d2)
    cd_repo.add_cookedDishes(d3)
    cd_repo.save()

    dr_repo.add_drinks(dr1)
    dr_repo.add_drinks(dr2)
    dr_repo.save()

    o1 = Order(1, 1, [1, 2, 3], [1, 2])
    print(o1.calc_cost(cd_repo, dr_repo))

main()