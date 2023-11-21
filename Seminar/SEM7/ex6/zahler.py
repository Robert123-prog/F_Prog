class Zahler:
    def __init__(self, counter):
        self.counter = counter

    def cnt(self):
        while self.counter <= 10:
            print(self.counter)
            self.counter += 1

        return self.counter

