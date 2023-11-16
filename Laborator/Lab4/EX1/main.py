from funcs.manual_draw import draw_man
from ui.menu import menu
#from funcs.auto_draw import ad


'''
scrie documentatie!!!!!
'''


def main():

   print(menu())

   ch = int(input('ch = '))

   if ch == 1:
       ad()

   if ch == 2:
        draw_man()

   else:
       return 0


main()
