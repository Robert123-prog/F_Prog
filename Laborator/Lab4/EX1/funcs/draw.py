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



