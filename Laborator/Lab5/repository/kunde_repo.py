from repository.datarepo import DataRepo
from modelle.kunde import Customer
import pickle

'''
in afara de read_file() si write_to_file() merge
vezi implementare convert_from_string()

'''

class CustomerRepo(DataRepo):

    def __init__(self):

        super().__init__("customers.txt")
        self.filename = self.__class__.__name__ + ".txt"
        self.customers = []

    def add_customers(self, customer: Customer):
        self.customers.append(customer)


    def save(self):
        with open(self.filename, 'wb') as f:
            for customer in self.customers:
                pickle.dump(customer, f)
                f.write(b'\n')  # Add a separator between objects

    '''
    except pickle.UnpicklingError handles errors that may occur during unpickling 
    (e.g., if the file format is corrupted or doesn't match the expected format). 
    
    When this happens:

    f.seek(position) resets the file position to where the last successful read occurred.

    f.readline() moves the file pointer to the start of the next line. 
    This is done to try and skip over the problematic data to continue reading the next valid object. 
    It assumes each object is on a separate line to help recover from the error.
    
    '''

    def load(self):
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # Get current file position
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # Reset file position if pickle fails
                    f.seek(position)
                    f.readline()  # Move to the next line

    def load_to_list(self): #se foloseste pentru search_after_partial_name
        self.customers = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # Get current file position
                try:
                    customer = pickle.load(f)
                    self.customers.append(customer)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    # Reset file position if pickle fails
                    f.seek(position)
                    f.readline()  # Move to the next line

        return self.customers


    def search_after_partial_name(self, partial_name):
        matching_customers = []
        all_customers = self.load_to_list()

        partial_name = partial_name.lower()

        for customer in all_customers:
            if partial_name in customer.name.lower():
                matching_customers.append(customer)

        return matching_customers

    def search_after_partial_address(self, partial_address):
        matching_addresses = []
        all_customers = self.load_to_list()

        partial_address = partial_address.lower()

        for customer in all_customers:
            if partial_address in customer.adresse.lower():
                matching_addresses.append(customer)

        return matching_addresses

    def update_cust_name(self, old_name: str, new_name: str):
        customers = self.load_to_list()

        for customer in customers:
            if customer.name == old_name:
                customer.name = new_name
                break

        with open(self.filename, 'wb') as f:
            for customer in customers:
                pickle.dump(customer, f)
                f.write(b'\n')  # Add a separator between objects


    # def read_file(self):
    #     f = open(self.filename, 'rb')
    #     file_content = f.read()
    #     content = []
    #     customer_data = file_content.split(b'\n')
    #
    #     for customer_data in customer_data: #verif daca lista cutomer_data are elemente
    #         customer = pickle.loads(customer_data)
    #         content.append(customer)
    #
    #     f.close()
    #     return content


    # def write_to_file(self, string):
    #     f = open(self.filename, 'ab')
    #     pickle.dump(string, f)
    #     f.write(b'\n')
    #     f.close()

    # def write_to_file(self, string):
    #     f = open(self.filename, 'ab')
    #
    #     if type(string) ==  str:
    #         f.write(string.encode() + b'\n')
    #     else:
    #         pickle.dump(string, f)
    #         f.write(b'\n')


    def convert_to_string(self):
        return [pickle.dumps(customer) for customer in self.customers]


    def convert_from_string(self, filename, string):
        pass

