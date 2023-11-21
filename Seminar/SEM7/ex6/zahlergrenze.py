class Zahlergrenze:
    def __init__(self, count_sec, count_min, count_h, grenze):
        self.count_sec = count_sec
        self.count_min = count_min
        self.count_h = count_h
        self.grenze = grenze

    def cnt_sec(self):

       while self.grenze > 0:

           for self.count_sec in range(0, 60, 1):
               print(self.count_sec)

           self.grenze -= 1
           print()



    def cnt_min(self):

        while self.grenze > 0:

            for self.count_min in range(0, 60, 1):
                print(self.count_min)

            self.grenze -= 1
            print()



    def cnt_h(self):

        while self.grenze > 0:

            for self.count_h in range(0, 60, 1):
                print(self.count_h)

            self.grenze -= 1
            print()



c = Zahlergrenze(0, 0, 0, 1)

print(c.count_h, " : ", c.count_min, " ; ", c.count_sec)



