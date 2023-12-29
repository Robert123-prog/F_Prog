from repository.datarepo import DataRepo
import pickle

class CustomerRepo(DataRepo):

    def __init__(self, filename: str):

        super().__init__()
        self.filename = self.__class__.__name__ + ".txt"
        self.customers = []

    def add_customers(self, customer):
        self.customers.append(customer)

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.customers, f)
        f.close()

    def load(self):
        f = open(self.filename, 'rb')
        self.customers = pickle.load(f)
        f.close()


    def read_file(self):
        file_content = []
        f = open(self.filename, 'rb')

        while True:

            try:
                current_obj = pickle.load(f)
                file_content.append(current_obj)
            except EOFError:
                break

        f.close()
        return file_content


    def write_to_file(self, string):
        f = open(self.filename, 'ab')
        pickle.dump(string, f)
        f.close()


    def convert_to_string(self):
        return list(map(lambda customer: pickle.dumps(customer), self.customers))


    def convert_from_string(self, filename, string):
        pass

