import pickle
from repository.datarepo import DataRepo



class OrderRepo(DataRepo):

    def __init__(self):

        super().__init__("orders.txt")
        self.filename = self.__class__.__name__ + ".txt"
        self.orders = []

    def add_orders(self, order):
        self.orders.append(order)

    def save(self):
        with open(self.filename, 'wb') as f:
            for order in self.orders:
                pickle.dump(order, f)
                f.write(b'\n')  # separa obiectele

    def load(self):
        orders = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # pozitia curenta din fisier
                try:
                    order = pickle.load(f)
                    self.orders.append(order)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  # citeste urmatoarea linie



    def load_to_list(self): #se foloseste pentru search_after_partial_name
        self.orders = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # pozitia curenta din fisier
                try:
                    order = pickle.load(f)
                    self.orders.append(order)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    # reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  # citeste urmatoarea linie

        return self.orders



    def read_file(self):
        f = open(self.filename, 'rb')
        file_content = []

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
        return [pickle.dumps(order) for order in self.orders]


    def convert_from_string(self, filename, string):
        pass


