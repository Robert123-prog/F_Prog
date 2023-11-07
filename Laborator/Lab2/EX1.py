'''
Functia "remove_rep" creeaza un vector nou in care introduce toate valorile unice din vectorul "vect"

Hard codat func perfect, dar daca dau eu ce valori vreau in lista imi adauga un zero la lista finala, cel mai probabil de la [0] * 20
'''


def remove_rep(vect):

    new_vect = []

    for i in range(len(vect) - 1):

        if vect[i] not in new_vect:

            new_vect.append(vect[i])

    return new_vect

def main():
    # l = [0] * 20
    # n = int(input('n = '))
    #
    # for j in range(n):
    #     l[j] = int(input('l[j] = '))
    #

    print(remove_rep([22, 44, 44, 10, 11, 22]))


main()


