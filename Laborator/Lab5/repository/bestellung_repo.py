import pickle

from repository.datarepo import DataRepo

class OrderRepo(DataRepo):

    def __init__(self, filename: str):

        super().__init__()
        self.filename = self.__class__.__name__ + ".txt"
        self.orders = []

    def add_orders(self, order):
        self.orders.append(order)

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.orders, f)
        f.close()
#pickle.dumps
#pickle.loads scrie in stringuri

    def load(self):
        f = open(self.filename, 'rb')
        self.drinks = pickle.load(f)
        f.close()


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
        return list(map(lambda order: pickle.dumps(order), self.orders))


    def convert_from_string(self, filename, string):
        pass

