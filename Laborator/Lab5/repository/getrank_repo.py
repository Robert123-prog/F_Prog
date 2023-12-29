from repository.datarepo import DataRepo
from modelle.getrank import Drink
import pickle

class DrinkRepo(DataRepo):

    def __init__(self):
        super().__init__("drinks.txt")
        self.filename = self.__class__.__name__ + ".txt"
        self.drinks = []

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def save(self):
        with open(self.filename, 'ab') as f:
            for drink in self.drinks:
                pickle.dump(drink, f)
                f.write(b'\n')  # Add a separator between objects


    def load(self):
        self.drinks = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # Get current file position
                try:
                    drink = pickle.load(f)
                    self.drinks.append(drink)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # Reset file position if pickle fails
                    f.seek(position)
                    f.readline()  # Move to the next line


    # def read_file(self):
    #     file_content = []
    #     f = open(self.filename, 'rb')
    #
    #     while True:
    #         try:
    #             current_object = pickle.load(f)
    #             file_content.append(current_object)
    #
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
        return [pickle.dumps(drink) for drink in self.drinks]


    def convert_from_string(self, filename, str_list):
        pass
        #cum plm convertesc un string la un obiect

dr1 = Drink(1, 10, 20)
dr2 = Drink(2, 15, 30)

repo = DrinkRepo()
repo.add_drinks(dr1)
repo.add_drinks(dr2)

repo.save()
repo.load()

for drink in repo.drinks:
    print(drink)