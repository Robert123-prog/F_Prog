import turtle

def ex1():
    t = turtle.Pen()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(35)
    t.right(90)
    t.forward(75)
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)

    turtle.exitonclick()

def ex2():
    t = turtle.Pen()
    t.up()
    t.left(90)
    t.forward(100)
    t.down()
    t.right(30)
    t.forward(20)
    t.right(30)
    t.forward(20)
    t.right(30)
    t.forward(20)
    t.right(30)
    t.forward(20)
    t.right(30)
    t.forward(20)
    t.right(30)
    t.forward(35)
    t.right(40)
    t.forward(120)
    t.up()
    t.right(140)
    t.forward(125)
    t.down()
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(20)
    t.left(30)
    t.forward(50)
    t.left(10)
    t.forward(80)

    turtle.exitonclick()


def ex3():
    t1 = turtle.Pen()
    t2 = turtle.Pen()

    '''
            Contur casa 1
            '''

    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(200)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(200)

    '''
        Contur casa 2
        '''
    t2.left(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(200)
    t2.right(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(200)

    '''

           Usa 1
           '''

    t1.right(180)
    t1.forward(75)
    t1.right(90)
    t1.forward(40)
    t1.left(90)
    t1.forward(30)
    t1.left(90)
    t1.forward(40)

    '''
           Usa 2
           '''
    t2.right(180)
    t2.forward(75)
    t2.left(90)
    t2.forward(40)
    t2.right(90)
    t2.forward(30)
    t2.right(90)
    t2.forward(40)

    '''
             Fereastra 1
            '''

    t1.left(90)
    t1.up()
    t1.forward(40)
    t1.left(90)
    t1.forward(60)
    t1.down()
    t1.forward(20)
    t1.right(90)
    t1.forward(20)
    t1.right(90)
    t1.forward(20)
    t1.right(90)
    t1.forward(20)

    '''
          Fereastra 2
          '''
    t2.left(90)
    t2.up()
    t2.forward(40)
    t2.left(90)
    t2.forward(60)
    t2.down()
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)
    t2.right(90)
    t2.forward(20)

    '''
            Acoperis 1
            '''
    t1.up()
    t1.backward(65)
    t1.right(90)
    t1.forward(40)
    t1.down()
    t1.left(60)
    t1.forward(115)
    t1.left(60)
    t1.forward(115)
    t1.left(60)


    '''
          Acoperis 2
          '''
    t2.up()
    t2.backward(55)
    t2.right(90)
    t2.forward(40)
    t2.down()

    t2.left(60)
    t2.forward(115)
    t2.left(60)
    t2.forward(115)

    t2.left(60)

    turtle.exitonclick()

def menu():
    return '''
        
        1 - Dreptunghi
        
        2 - Inima
        
        3 - Case
    '''

def main():
    print(menu())
    ch = int(input('ch = '))

    if ch == 1:
        ex1()

    elif ch == 2:
        ex2()

    elif ch == 3:
        ex3()

    else:
        print('Invalid number')

main()
