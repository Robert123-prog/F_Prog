from repository.datarepo import DataRepo
import pickle

class DrinkRepo(DataRepo):

    def __init__(self):
        super().__init__("drinks.txt")
        self.filename = self.__class__.__name__ + ".txt"
        self.drinks = []

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def save(self):
        with open(self.filename, 'wb') as f:
            for drink in self.drinks:
                pickle.dump(drink, f)
                f.write(b'\n')  # Add a separator between objects


    def load(self):
        self.drinks = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  # pozitia curenta din fisier
                try:
                    drink = pickle.load(f)
                    self.drinks.append(drink)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                        # reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  # citeste urmatoarea linie

    def get_drink_id(self, drink_id):
        for drink in self.drinks:
            if drink.id == drink_id:
                return drink

    def load_to_list(self): #se foloseste pentru search_after_partial_name
        self.drinks = []
        with open(self.filename, 'rb') as f:
            while True:
                position = f.tell()  #pozitia curenta din fisier
                try:
                    drink = pickle.load(f)
                    self.drinks.append(drink)
                except EOFError:
                    break
                except pickle.UnpicklingError:
                    #  reseteaza pozitia din fisier daca UnpicklingError
                    f.seek(position)
                    f.readline()  # citeste urmatoarea linie

        return self.drinks


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
        return [pickle.dumps(drink) for drink in self.drinks]


    def convert_from_string(self, filename, str_list):
        pass


