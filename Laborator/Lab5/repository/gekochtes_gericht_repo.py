import pickle

from repository.datarepo import DataRepo

class CookedDishRepo(DataRepo):

    def __init__(self, filename: str):

        super().__init__()
        self.filename = self.__class__.__name__ + ".txt"
        self.cookedDishes = []

    def add_cookedDishes(self, cooked_dish):
        self.cookedDishes.append(cooked_dish)

    def save(self):
        f = open(self.filename, 'ab')
        pickle.dump(self.cookedDishes, f)
        f.close()


    def load(self):
        f = open(self.filename, 'rb')
        self.cookedDishes = pickle.load(f)
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
        return list(map(lambda cooked_dish: pickle.dumps(cooked_dish), self.cookedDishes))



    def convert_from_string(self, filename, str_list):
        pass

