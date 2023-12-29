from repository.datarepo import DataRepo
import pickle

class DrinkRepo(DataRepo):

    def __init__(self):
        super().__init__()
        self.filename = self.__class__.__name__ + ".txt"
        self.drinks = []

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.drinks, f)
        f.close()


    def load(self):
        f = open(self.filename, 'rb')
        self.drinks = pickle.load(f)
        f.close()


    def read_file(self):
        file_content = []
        f = open(self.filename, 'rb')

        while True:
            try:
                current_object = pickle.load(f)
                file_content.append(current_object)

            except EOFError:
                break

        f.close()
        return file_content


    def write_to_file(self, string):
        f = open(self.filename, 'ab')
        pickle.dump(string, f)
        f.close()


    def convert_to_string(self):
         return list(map(lambda drink: pickle.dumps(drink), self.drinks))


    def convert_from_string(self, filename, str_list):
        pass
        #cum plm convertesc un string la un obiect

