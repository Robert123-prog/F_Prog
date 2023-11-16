import turtle

t = turtle.Pen()
t.speed(3)



def A(t):
    t.up()
    t.forward(7)
    t.down()
    t.forward(15)
    t.back(15)
    t.left(60)
    t.back(17)
    t.forward(34)
    t.right(120)
    t.forward(34)
    t.back(17)

    t.left(60)  # zuruck nach rechts fur den nachsten Buchstaben
    t.up()
    t.forward(21)
    t.down()

def B(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(10)

    t.right(45)
    t.forward(3)
    t.left(90)
    t.forward(3)
    t.right(45)

    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(10)
    t.right(90)
    t.up()
    t.forward(15)
    t.right(90)
    t.forward(2)
    t.down()
    t.forward(12)

    t.up()
    t.forward(17)
    t.down()


def C(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.back(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def D(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(15)
    t.right(30)
    t.forward(5)
    t.right(60)
    t.forward(26)
    t.right(60)
    t.forward(5)
    t.right(30)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def E(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.back(20)


    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(15)
    t.down()


def F(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.back(20)
    t.down()

    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(15)
    t.down()


def G(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(17)
    t.down()
    t.left(90)
    t.back(8)
    t.forward(8)
    t.right(90)
    t.forward(13)
    t.left(90)
    t.back(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def H(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def I(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def J(t):
    t.up()
    t.right(90)
    t.forward(5)
    t.down()
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def K(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)
    t.right(45)
    t.forward(20)
    t.back(20)
    t.right(90)
    t.forward(20)
    t.back(20)
    t.left(45)

    t.up()
    t.forward(35)
    t.down()


def L(t):
    t.left(90)
    t.forward(15)
    t.back(30)
    t.right(90)
    t.forward(20)
    t.back(20)
    t.left(90)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(35)
    t.down()


def M(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(135)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(135)
    t.forward(30)
    t.back(15)

    t.up()
    t.left(90)
    t.forward(15)
    t.down()


def N(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(150)
    t.forward(35)
    t.left(150)
    t.forward(30)

    t.up()
    t.back(15)
    t.right(90)
    t.forward(15)
    t.down()


def O(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def P(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(13)
    t.right(90)
    t.forward(20)

    t.up()
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(35)
    t.down()


def Q(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.up()
    t.forward(5)
    t.right(135)
    t.down()
    t.forward(10)
    t.back(10)
    t.left(135)
    t.up()
    t.back(5)
    t.down()
    t.left(90)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def R(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(13)
    t.right(90)
    t.forward(20)
    t.left(135)
    t.forward(24)
    t.back(22)

    t.up()
    t.left(45)
    t.forward(35)
    t.down()


def S(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.back(20)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def T(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.back(10)
    t.right(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.left(90)
    t.forward(25)
    t.down()


def U(t):
    t.left(90)
    t.forward(15)
    t.back(30)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def V(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.right(150)
    t.down()
    t.forward(30)
    t.left(120)
    t.forward(32)

    t.up()
    t.back(18)
    t.right(60)
    t.forward(20)
    t.down()


def W(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.right(165)
    t.down()
    t.forward(30)
    t.left(150)
    t.forward(30)
    t.right(150)
    t.forward(30)
    t.left(150)
    t.forward(30)

    t.up()
    t.back(16)
    t.right(75)
    t.forward(17)
    t.down()


def X(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(150)
    t.forward(36)
    t.up()
    t.left(150)
    t.forward(31)
    t.down()
    t.left(150)
    t.forward(36)

    t.up()
    t.back(19)
    t.left(120)
    t.forward(22)
    t.down()


def Y(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(150)
    t.forward(15)
    t.left(120)
    t.forward(15)
    t.back(15)
    t.right(150)
    t.forward(17)

    t.up()
    t.back(15)
    t.left(90)
    t.forward(20)
    t.down()


def Z(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(90)
    t.forward(20)
    t.left(245)
    t.forward(32)
    t.right(245)
    t.forward(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.down()


def Space(t):
    t.up()
    t.forward(15)
    t.down()


def Dot(t):
     t.up()
     t.right(90)
     t.forward(13)
     t.down()
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.right(90)

     t.up()
     t.forward(13)
     t.right(90)
     t.forward(15)
     t.down()


def Quesmark(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(17)
    t.up()
    t.forward(2)
    t.down()
    t.forward(1)

    t.up()
    t.back(15)
    t.left(90)
    t.forward(30)
    t.down()


def Exclamation(t):
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(180)
    t.forward(25)
    t.up()
    t.forward(3)
    t.down()
    t.forward(2)
    t.up()
    t.back(15)
    t.left(90)
    t.forward(20)
    t.down()

def New_Paragraph(t):
    t.up()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(730)
    t.right(180)
    t.down()




d = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,'K': K,'L': L,
'M': M, 'N': N,'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,'U': U,'V': V, 'W': W, 'X': X, 'Y': Y, 'Z':Z, ' ': Space,
     '.': Dot, '?': Quesmark, '!': Exclamation}

def ad():
    word = input("word = ")

    word = word.upper()
    l = list(word)

    begin(t)

    for letter in l:

        if letter in d:
            d[letter](t)

    turtle.done()


def begin(t):
    t.up()
    t.forward(-300)
    t.down()

def save_input_man(input):
    with open('history.txt', 'a') as f:
        f.write(input + '\n')


def menu():
    return '''
        1 - Draw automatically

        2 - Draw yourself

    '''

import turtle


def fwd(t):
    with open('history.txt', 'a') as f:
        f.write('w')

    t.speed(1)
    t.forward(10)

def bckw(t):
    with open('history.txt', 'a') as f:
        f.write('s')
    t.speed(1)
    t.forward(-10)

def rotright(t):
    with open('history.txt', 'a') as f:
        f.write('d')
    t.speed(1)
    t.right(45)

def rotleft(t):
    with open('history.txt', 'a') as f:
        f.write('a')
    t.speed(1)
    t.left(45)

def pup(t):
    with open('history.txt', 'a') as f:
        f.write('f')
    t.speed(1)
    t.up()

def pdown(t):
    with open('history.txt', 'a') as f:
        f.write('g')
    t.speed(1)
    t.down()



def keys():
    t = turtle.Pen()
    turtle.onkey(fwd, 'w')
    turtle.onkey(bckw, 's')
    turtle.onkey(rotright, 'd')
    turtle.onkey(rotleft, 'a')
    turtle.onkey(pup, 'f')
    turtle.onkey(pdown, 'g')

def draw_man():

    keys()
    turtle.listen()
    turtle.done()

'''
scrie documentatie!!!!!
'''

import turtle

# (Your drawing functions)

def begin(t):
    t.up()
    t.forward(-300)
    t.down()

def save_input_man(input):
    with open('history.txt', 'a') as f:
        f.write(input + '\n')

def menu():
    return '''
        1 - Draw automatically
        2 - Draw yourself
    '''

def draw_man():
    t = turtle.Pen()
    keys(t)
    turtle.listen()
    turtle.done()

def keys(t):
    turtle.onkey(lambda: fwd(t), 'w')
    turtle.onkey(lambda: bckw(t), 's')
    turtle.onkey(lambda: rotright(t), 'd')
    turtle.onkey(lambda: rotleft(t), 'a')
    turtle.onkey(lambda: pup(t), 'f')
    turtle.onkey(lambda: pdown(t), 'g')

def ad():
    word = input("word = ")
    word = word.upper()
    l = list(word)
    t = turtle.Pen()
    begin(t)
    for letter in l:
        if letter in d:
            d[letter](t)
    turtle.done()

def main():
    print(menu())
    ch = int(input('ch = '))
    if ch == 1:
        ad()
    elif ch == 2:
        draw_man()
    else:
        return 0

if __name__ == "__main__":
    main()


def main():

   print(menu())

   ch = int(input('ch = '))

   if ch == 1:
       ad()

   if ch == 2:
        draw_man()

   else:
       return 0


main()






