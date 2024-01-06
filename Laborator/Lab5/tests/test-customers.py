'''
Test to see if functionalities regarding customers work
'''

from modelle.kunde import Customer
from repository.kunde_repo import CustomerRepo

c1 = Customer(1, 'David', 'Lazaret')
c2 = Customer(2, 'Robert', 'Livezii')

repo = CustomerRepo()

def test_search_after_name():
    repo.add_customers(c1)
    repo.add_customers(c2)
    repo.save()

    name = input('Enter name: ')
    matching_customers = repo.search_after_partial_name_filt2(name)

    #assert len(matching_customers) == 0 #Error
    assert len(matching_customers) != 0

#test_search_after_name()

def test_search_after_address():
    repo.add_customers(c1)
    repo.add_customers(c2)
    repo.save()

    address = input('Enter address: ')
    matching_addresses = repo.search_after_partial_address(address)

    #assert len(matching_addresses) == 0 #Error
    assert len(matching_addresses) != 0

#test_search_after_address()

def test_name_update():
    repo.add_customers(c1)
    repo.add_customers(c2)
    repo.save()

    old_name = input('Enter old name: ')
    new_name = input('Enter new name: ')

    old_names = repo.load_to_list()
    repo.update_cust_name(old_name, new_name)
    new_names = repo.load_to_list()

    assert old_names != new_names
    #assert old_names == new_names #Error

test_name_update()

