from ui.menu import menu
from funcs.auto_draw import ad

'''
ad func, scrie documentatie!!!!!
'''


def main():

   print(menu())

   ch = int(input('ch = '))

   if ch == 1:
       ad()

   if ch == 2:
        pass

   else:
       return 0


main()
