from ex3.ui.menu import menu

import random

l = ["Rock", "Paper", "Scissors"]

'''
alegerea jucatorului din lista "l"
'''
def h_choice(list, ch):


    if ch == 1:
        print("Rock")
        return list[0]

    elif ch == 2:
        print("Paper")
        return list[1]

    elif ch == 3:
        print("Scissors")
        return list[2]

    else:
        return "Invalid choice"


'''
alegerea aleatorie a calculatorului din lista l trimisa ca parametrul "list"
'''
def c_choice(list):

    return random.choice(list)


def match():

    ctc = 0
    cth = 0

    '''
    se joaca pana cand unul dintre jucatori ajunge la 2 puncte
    '''

    while cth < 2 and ctc < 2:
       print(menu())

       ch = int(input('ch = '))

       ch1 = h_choice(l, ch)
       ch2 = c_choice(l)


       '''
       Toate variantele posibile de alegeri
       '''

       if ((ch1 == 'Rock' and ch2 == 'Paper') or
                (ch1 == 'Paper' and ch2 == 'Scissors') or
                (ch1 == 'Scissors' and ch2 == 'Rock')):
                 ctc += 1
                 print(ch2)
                 print("comp: ", ctc, " : ","you:", cth)

       elif ((ch1 == 'Rock' and ch2 == 'Scissors') or
              (ch1 == 'Paper' and ch2 == 'Rock') or
              (ch1 == 'Scissors' and ch2 == 'Paper')):
            cth += 1
            print(ch2)
            print("comp: ", ctc, " : ", "you:", cth)

       else:
            print(ch2)
            print("Draw")
            print("comp: ", ctc, " : ", "you:", cth)

    if ctc > cth:
        print("You lose!")

    else:
        print("You win!")