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

def h_rock(list):
    print("Rock")
    return list[0]

def h_paper(list):
    print("Paper")
    return list[1]

def h_scissors(list):
    print("Scissors")
    return list[2]


def c_choice(list):

    ch = random.choice(list)

    if ch == 1:
        print(list[0])
        return list[0]

    elif ch == 2:
        print(list[1])
        return list[1]

    else:
        print(list[2])
        return list[2]

def menu():
    return '''
    
        1 - Rock
        
        2 - Paper
        
        3 - Scissors 
        
    '''


def match(cth, ctc):

    for i in range(3):
        print(menu())

        ch = int(input('ch ='))
        c_choice(l)

        if ch == 1:
            h_rock(l)


            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1
                print("You lose")

            elif (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1
                print("You win")

        elif ch == 2:
            h_paper(l)


            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1
                print("You lose")

            elif (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1
                print("You win")

        elif ch == 3:
            h_scissors(l)


            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1
                print("You lose")

            elif (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1
                print("You win")

        else:
            print("Invalid option!")

    if ctc > cth:
        return "Computer wins"

    else:
        return "You win"

def main():
    match(0, 0)

main()