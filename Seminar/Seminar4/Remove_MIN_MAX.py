"""
Documentatie
"""



def calc_max(vect):
    mx = 0

    for i in vect:

        if i >= mx:

            mx = i

    return mx

def test_calc_max():
    assert calc_max([1, 2, 5, 9, 10, 11, 3, 4]) == 11

def calc_min(vect):
    mn = 99999999999

    for i in vect:

        if i <= mn:

            mn = i

    return mn

def test_calc_min():
    assert calc_min([1, 2, 5, 9, 10, 11, 3, 4]) == 1



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

def menu():
    return '''
        0 - exit
        
        1 - show list
        
        2 - del elements from list
        
        3 - return min from list
        
        4 - return max from list 
    
    '''

def main():
    n = int(input('n = '))
    l = []

    for i in range(n):
        l.append(int(input('el = ')))



    while True:

        print(menu())
        ch = int(input("ch = "))

        if ch == 0:
            break

        if ch == 1:

            print(l)


        if ch == 2:
            ct = int(input("How many elements to be removed: "))
            poz = int(input("Index of first element: "))
            rem_from_list(l, poz, ct)

        if ch == 3:
            print(calc_min(l))

        if ch == 4:
            print(calc_max(l))





main()
