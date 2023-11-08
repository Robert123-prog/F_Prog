
def repl(word, new_word, filename):

    ct = 0

    with open(filename, 'r') as f:
        content = f.read()

    with open(filename, 'w') as f:
        new_content = content.replace(word, new_word)

    with open(filename, 'r') as f:
        for w in filename:
            if w == new_word:
                ct += 1

    return ct

def main():

    f = open("data.txt", 'r')

    word = input("word = ")
    new_word = input("new word = ")

    repl(word, new_word, f)


    f.close()

main()


