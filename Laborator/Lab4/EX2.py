'''
merge fara contor
'''


def repl(word, new_word):

    with open("data.txt", 'r') as f:
        words = f.read()

        words = words.replace(word, new_word)

    with open("data.txt", 'w') as f:
        f.write(words)

def count(new_word):

    ct = 0

    with open("data.txt", 'r') as f:

        for word in f:

            if word == new_word:
                ct += 1

    return ct

def main():

    word = input("word = ")
    new_word = input("new word = ")

    repl(word, new_word)
    count(new_word)

main()