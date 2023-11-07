'''
Functia "cifre_din_elem" creeaza o lista cu cifrele din toate elementele din vectorul dat

Functia "sort_list" ordoneaza descrescator toate cifrele din output-ul functiei de mai sus

Functia "list_to_str" transforma lista sortata intr-un string (de fapt int)
'''

def cifre_din_elem(vect):

    vect_cif = []

    for i in vect:

        while i > 0:
            vect_cif.append(i % 10)
            i //= 10

    return vect_cif

def sort_list(vect):

    for i in range(len(vect) - 1):

        for j in  range(i + 1, len(vect), 1):

            if vect[i] < vect[j]:
                vect[i], vect[j] = vect[j], vect[i]


    return vect

def list_to_str(vect):

    nr = 0

    for i in vect:

        nr = nr * 10 + i

    return nr

def main():
   print(list_to_str(sort_list(cifre_din_elem([10, 33, 41, 87, 15]))))

main()