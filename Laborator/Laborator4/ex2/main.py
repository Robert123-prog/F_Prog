from ex2.replace import repl


def main():
    word = input("word = ")
    new_word = input("new word = ")

    count = repl(word, new_word)
    print(count)

main()