'''
Test to see if the add cooked Dish functionality works
'''

from modelle.gekochtes_gericht import Cooked_Dish
from repository.gekochtes_gericht_repo import CookedDishRepo

d1 = Cooked_Dish(1, 100, 15, 350)
d2 = Cooked_Dish(2, 200, 20, 350)

repo = CookedDishRepo()

def test_add_to_list():
    repo.add_cookedDishes(d1)
    repo.add_cookedDishes(d2)

    assert len(repo.cookedDishes) != 0
    #assert len(repo.cookedDishes) == 0 #Error

#test_add_to_list()

def test_add_to_file():
    repo.add_cookedDishes(d1)
    repo.add_cookedDishes(d2)
    repo.save()

    assert repo.filename
    #assert not repo.filename #Error

test_add_to_file()
