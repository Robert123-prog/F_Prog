
def repl(word, new_word):
    with open("data.txt", 'r') as f:
        words = f.read()
        modified_words = words.replace(word, new_word)


    count = modified_words.count(new_word)


    with open("data.txt", 'w') as f:
        f.write(modified_words)

    return count

def main():
    word = input("word = ")
    new_word = input("new word = ")

    count = repl(word, new_word)
    print(count)

main()