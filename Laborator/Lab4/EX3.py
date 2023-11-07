import random


l = ["Rock", "Paper", "Scissors"]
# def h_choice(list, ch):
#
#     if ch == 1:
#         return list[0]
#
#     elif ch == 2:
#         return list[1]
#
#     elif ch == 3:
#         return list[2]
#
#     else:
#         return "Invalid choice"

def h_rock(list):
    return list[0]

def h_paper(list):
    return list[1]

def h_scissors(list):
    return list[2]


def c_choice(list):

    ch = random.choice(list)

    if ch == 1:
        return list[0]

    elif ch == 2:
        return list[1]

    else:
        return list[2]

def menu():
    return '''
        1 - Rock
        2 - Paper
        3 - Scissors 
    '''


def match(cth, ctc):

    while cth < 2 or ctc < 2:
        print(menu())

        ch = int(input('ch ='))

        if ch == 1:
            h_rock(l)
            c_choice(l)

            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1

            if (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1

        if ch == 2:
            h_paper(l)
            c_choice(l)

            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1

            if (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1

        if ch == 3:
            h_scissors(l)
            c_choice(l)

            if (h_rock(l) and c_choice(l) == "Paper") or (
                    h_paper(l) and c_choice(l) == "Scissors") or (
                    h_scissors(l) and c_choice(l) == "Rock"):
                ctc += 1

            if (h_rock(l) and c_choice(l) == "Scissors") or (
                    h_paper(l) and c_choice(l) == "Rock") or (
                    h_scissors(l) and c_choice(l) == "Paper"):
                cth += 1


    if ctc > cth:
        return "Computer wins"

    else:
        return "You win"

def main():
    match(0, 0)