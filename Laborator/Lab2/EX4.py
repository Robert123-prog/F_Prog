
'''
Criptare cu +
'''

# def criptare_plus(vect):
#
#      t = vect[0]
#
#      for i in range(1, len(vect)):
#          vect[i] += t
#
#      return vect
#
#
# def main():
#      print(criptare_plus([12, 15 ,15, 10, 12, 20]))
#
# main()
#
# '''
# Criptare cu *
# '''
#
def criptare_inmultit(vect):

     t = vect[0]

     for i in range(1, len(vect)):
         vect[i] *= t

     return vect

def main():
    print(criptare_inmultit([5, 8, 10, 4, 6, 7]))
main()


'''
 Criptare cu XOR
'''

# def cript(vect):
#
#     t = vect[0]
#
#     for i in range(1, len(vect)):
#
#         vect[i] = t ^ vect[i]
#
#     return vect
#
# def main():
#     print(cript([12, 15, 13]))

# main()