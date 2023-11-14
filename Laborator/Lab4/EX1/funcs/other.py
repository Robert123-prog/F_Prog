def begin(t):
    t.up()
    t.forward(-300)
    t.down()

def save_input(input):
    with open('history.txt', 'a') as f:
        f.write(input + '\n')