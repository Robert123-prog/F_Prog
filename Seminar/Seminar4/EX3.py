'''
Documentatie
'''

def rem_from_list(vect, poz, ct):
    while ct > 0:
        vect.pop(poz)
        ct -= 1

        if ct > 0:
            poz = int(input('poz = '))

    return vect

def main():
    ct = int(input('cate elemente = '))
    poz = int(input('poz = '))

    print(rem_from_list([1, 2, 4 ,2, 5, 9, 10, 11, 13], poz, ct))

main()