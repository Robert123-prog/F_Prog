import pickle
from modelle.bestellung import Order
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
                f.write(b'\n')  # Add a separator between objects

    def load(self):
        self.orders = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # Get current file position
                try:
                    order = pickle.load(f)
                    self.orders.append(order)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # Reset file position if pickle fails
                    f.seek(position)
                    f.readline()  # Move to the next line



    # def read_file(self):
    #     f = open(self.filename, 'rb')
    #     file_content = []
    #
    #     while True:
    #
    #         try:
    #             current_obj = pickle.load(f)
    #             file_content.append(current_obj)
    #         except EOFError:
    #             break
    #
    #     f.close()
    #     return file_content
    #
    #
    # def write_to_file(self, string):
    #     f = open(self.filename, 'ab')
    #     pickle.dump(string, f)
    #     f.close()


    def convert_to_string(self):
        return [pickle.dumps(order) for order in self.orders]


    def convert_from_string(self, filename, string):
        pass

o1 = Order(1, 1, [1, 2], [1, 2])
o2 = Order(2, 2, [1], [2])

repo = OrderRepo()
repo.add_orders(o1)
repo.add_orders(o2)

repo.save()
repo.load()

for order in repo.orders:
    print(order)
