'''
Functia check_domino verifica daca 2 nr oarecare sunt de tip "domino"

Functia check_domino_vect verifica daca 2 el vecine dintr-un vector oarecare sunt de tip "domino", cu ajutorul functiei check_domino

In final, fct check_domino_vect calculeaza lungimea maxima a secventei cerute
'''




def check_domino(nr1, nr2):

    if nr1 % 10 == (nr2 // 10) % 10:
        return True

    return False

def check_domino_vect(vect):
    lg = 1
    lgmax = 1

    for i in range(len(vect) - 1):

        if check_domino(vect[i], vect[i + 1]) == True:
            lg += 1

        else:
            lg = 1

        if lg > lgmax:
            lgmax = lg

    return lgmax

def test():
    assert check_domino_vect([89, 95, 54, 10]) == 3

def main():
    print(check_domino_vect([89, 95, 54, 10, 12, 24, 42, 26, 67]))

main()