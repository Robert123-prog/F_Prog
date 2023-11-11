import random

l = ["Rock", "Paper", "Scissors"]
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


def c_choice(list):

    return random.choice(list)

def menu():
    return '''
    
        1 - Rock
        
        2 - Paper
        
        3 - Scissors 
        
    '''


def match():

    ctc = 0
    cth = 0

    while cth < 2 and ctc < 2:
       print(menu())

       ch = int(input('ch = '))

       ch1 = h_choice(l, ch)
       ch2 = c_choice(l)


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

def main():
    match()

main()