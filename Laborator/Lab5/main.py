from modelle.kunde import Customer
from repository.kunde_repo import CustomerRepo

def main():
   c1 = Customer(1, 'David', 'Lazaret')
   c2 = Customer(2, 'Robert', 'Livezii')
   c3 = Customer(3, 'Davdutz', 'Livezii')


   repo = CustomerRepo()

   repo.add_customers(c1)
   repo.add_customers(c2)
   repo.add_customers(c3)
   repo.save()

   #metoda de update name inca nu merge
   #CAUTARILE DUPA CLIENTI SI ADRESE TREBUIE FACUTE CU FILTER()
   #NU LE STERGE PE CELE EXISTENTE DACA NU MERGE CU FILTER
   #MAI VEZI METODELE DE WRITE SI CONVERT:((((

   # repo.update_cust_name('David', 'Dani')
   # repo.update_cust_name('Robert', 'Radu')


   # cust = repo.load_to_list()
   # print(cust)

main()

