import turtle

t = turtle.Pen()

'''
am definit functiile pentru miscarea pe interfata turtle
functia "draw_man" foloseste turtleonkeypress si listen() pentru a asocia fiecarei litere de la tastaura functia corespunzatoare
'''

def fwd():
    with open('history.txt', 'a') as f:
        f.write('w')

    t.speed(1)
    t.forward(10)

def bckw():
    with open('history.txt', 'a') as f:
        f.write('s')
    t.speed(1)
    t.forward(-10)

def rotright():
    with open('history.txt', 'a') as f:
        f.write('d')
    t.speed(1)
    t.right(45)

def rotleft():
    with open('C:\Proiecte\Proiecte faculta\Python\PycharmProjects\Laborator\Laborator4\ex1\history.txt', 'a') as f:
        f.write('a')
    t.speed(1)
    t.left(45)

def pup():
    with open('history.txt', 'a') as f:
        f.write('f')
    t.speed(1)
    t.up()

def pdown():
    with open('history.txt', 'a') as f:
        f.write('g')
    t.speed(1)
    t.down()



def draw_man():
    turtle.onkeypress(fwd, 'w')
    turtle.onkeypress(bckw, 's')
    turtle.onkeypress(rotright, 'd')
    turtle.onkeypress(rotleft, 'a')
    turtle.onkeypress(pup, 'f')
    turtle.onkeypress(pdown, 'g')

    turtle.listen()
    turtle.done()
    with open('C:\Proiecte\Proiecte faculta\Python\PycharmProjects\Laborator\Laborator4\ex1\history.txt', 'a') as f:
        f.write('\n')


