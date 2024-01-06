from repository.datarepo import DataRepo
from modelle.kunde import Customer
import pickle



class CustomerRepo(DataRepo):

    def __init__(self):

        super().__init__("CustomerRepo.txt")
        self.customers = []

    def add_customers(self, customer: Customer):
        self.customers.append(customer)


    def save(self):
        with open(self.filename, 'wb') as f:
            for customer in self.customers:
                pickle.dump(customer, f)
                f.write(b'\n')  # Add a separator between objects

    '''
    
    except pickle.UnpicklingError folosit pentru exceptiile care pot aparea cand dau load()
    
    Daca e cazul:

    f.seek(position) reseteaza pozitia fisierului acolo unde s-a intamplat ultima citire care nu a dat eroare

    f.readline() muta pointerul din fisier la inceputul liniei urmatoare 
    
    '''

    def load(self):
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # pozitia curenta din fisier
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  #citeste urmatoarea linie

    def load_to_list(self): #se foloseste pentru search_after_partial_name
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # pozitia curenta din fisier
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    # reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  # citeste urmatoarea linie

        return self.customers

    '''
    fara filter()
    '''

    def search_after_partial_name(self, partial_name):
        matching_customers = []
        all_customers = self.load_to_list()

        partial_name = partial_name.lower()

        for customer in all_customers:
            if partial_name in customer.name.lower():
                matching_customers.append(customer)

        return matching_customers


    '''
    cu filter()
    '''

    def search_after_partial_name_filt2(self, partial_name):
        all_customers = self.load_to_list()

        matching_customers = filter(lambda customer: partial_name in customer.name, all_customers)

        matching_customers = list(matching_customers)

        return matching_customers

    '''
    fara filter()
    '''

    def search_after_partial_address(self, partial_address):
        matching_addresses = []
        all_customers = self.load_to_list()

        partial_address = partial_address

        for customer in all_customers:
            if partial_address in customer.adresse:
                matching_addresses.append(customer)

        return matching_addresses

    '''
    cu filter()
    '''

    def search_after_partial_address_with_filter(self, partial_address):
        all_customers = self.load_to_list()

        matching_addresses = filter(lambda customer: partial_address in customer.adresse, all_customers)

        matching_addresses = list(matching_addresses)

        return matching_addresses

    def update_cust_name(self, old_name: str, new_name: str):
        customers = self.load_to_list()

        for customer in customers:
            if customer.name == old_name:
                customer.name = new_name
                break
        self.save()


    def read_file(self):
        f = open(self.filename, 'rb')
        file_content = f.read()
        content = []
        customer_data = file_content.split(b'\n')

        for customer_data in customer_data: #verif daca lista cutomer_data are elemente
            customer = pickle.loads(customer_data)
            content.append(customer)

        f.close()
        return content

    def write_to_file(self, string):
        f = open(self.filename, 'ab')

        if type(string) ==  str:
            f.write(string.encode() + b'\n')
        else:
            pickle.dump(string, f)
            f.write(b'\n')


    def convert_to_string(self):
        return [pickle.dumps(customer) for customer in self.customers]


    def convert_from_string(self, filename, string):
        pass

