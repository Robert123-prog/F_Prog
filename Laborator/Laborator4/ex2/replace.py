
def repl(word, new_word):
    with open("data.txt", 'r') as f:
        words = f.read()
        modified_words = words.replace(word, new_word)


    count = modified_words.count(new_word)


    with open("data.txt", 'w') as f:
        f.write(modified_words)

    return count

