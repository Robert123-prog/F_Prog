'''
Functia "sim" verifica daca 2 variable oarecare sunt simetrice

Functia "sim_list" calculeaza numarul de el simetrice dintr-un vector, folosind functia "sim"
'''

def sim(nr1, nr2):

    if nr1 % 10 == (nr2 // 10) % 10 and nr2 % 10 == (nr1 // 10) % 10:
        return True

    return False

def sim_list(vect):
    ct = 0

    for i in range(len(vect) - 1):

        for j in range(i + 1, len(vect), 1):

            if (sim(vect[i], vect[j])) == True:
                ct += 1

    return ct

def main():

    print(sim_list([12, 21, 33, 10, 56, 65, 23, 32, 21]))

main()