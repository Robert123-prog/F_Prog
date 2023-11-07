
# nooope
#['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# def reverse(word):
#
#     l = list(word)
#     poz = len(l) - 1
#     for i in range((len(l) - 1) // 2):
#
#        if l[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#
#             for j in range(poz, (len(l) - 1) // 2 , -1):
#
#                 if l[j] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#
#                     l[i], l[j] = l[j], l[i]
#                     poz = j - 1
#                     break
#
#
#     newword = str(l)
#     return newword
#
# print(reverse('Terminator'))

'''
Incercare cu sim unui elem intr o lista- merig oe pista asta ca parca iese
'''

def rev(word):
    l = list(word)
    poz = len(l) - 1

    for i in range(len(l)):

        if l[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] and l[len(l) - i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:

            l[i], l[len(l) - i] = l[len(l) - i], l[i]

    newword = str(l)
    return newword

print(rev("Terminator"))