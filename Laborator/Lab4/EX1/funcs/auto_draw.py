from funcs.characters import *
from funcs.other import *

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


# if __name__ == "__main__":
#     ad()



