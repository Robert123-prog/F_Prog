class UI:
    def __init__(self, choice):
        self.choice = choice


    def run(self):
        pass

    # def main_menu(self):
    #     print("""
    #
    #          1. Orders
    #          2. Database
    #
    #
    #         """)
    #
    # def orders(self):
    #     print("""
    #
    #         1. Save Order
    #         2. Load Order
    #         3. Add Order
    #
    #         """)
    #
    # def database(self):
    #     print('''
    #
    #         1. Modify Menu
    #         2. Modify Customers
    #
    #          ''')
    #
    # def menu(self):
    #     print("""
    #
    #         1. Modify Dishes
    #         2. Modify Cooked Dishes
    #         3. Modify Drinks
    #
    #         """)
    #
    # def dishes(self):
    #     print("""
    #
    #         1. Save Dish
    #         2. Load Dish
    #         3. Add Dish
    #
    #         """)
    #
    # def cooked_dishes(self):
    #     print("""
    #
    #         1. Save Cooked Dish
    #         2. Load Cooked Dish
    #         3. Add Cooked Dish
    #
    #         """)
    #
    # def drinks(self):
    #     print("""
    #
    #         1. Save Drink
    #         2. Load Drink
    #         3. Add Drink
    #
    #         """)
    #
    # def customers(self):
    #     print("""
    #
    #         1. Save Customer
    #         2. Load Customer
    #         3. Add Customer
    #
    #         """)












# '''
# mch - choice pe cum ar veni branchul principal
# ich - choice pe fiecare brach in parte din meniu
# ui trebuie facut ca si o clasa:((((
# '''
#
# def menu():
#
#
#
#     print( """
#
#     1. Orders
#     2. Database
#
#
#     """)
#
#     mch = int(input('ch = '))
#
#     if mch == 1:
#         pass
#
#     else:
#         print('''
#
#         1. Modify Menu
#         2. Modify Customers
#
#         ''')
#
#         mch1 = int(input('ch1 = '))
#
#         if mch1 == 1:
#             print("""
#
#             1. Modify Dishes
#             2. Modify Cooked Dishes
#             3. Modify Drinks
#
#             """)
#
#             ich1 = int(input('ich1 = '))
#
#             if ich1 == 1:
#                 print("""
#
#                 1. Save Dish
#                 2. Load Dish
#                 3. Add Dish
#
#                 """)
#
#             elif ich1 == 2:
#                 print("""
#
#                 1. Save Cooked Dish
#                 2. Load Cooked Dish
#                 3. Add Cooked Dish
#
#                 """)
#
#             else:
#                 print("""
#
#                 1. Save Drink
#                 2. Load Drink
#                 3. Add Drink
#
#                 """)
#
#         else:
#             print("""
#
#             1. Save Customer
#             2. Load Customer
#             3. Add Customer
#
#             """)
#
#
#
# menu()