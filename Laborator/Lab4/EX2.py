
def repl(word, new_word):
    with open("data.txt", 'r') as f:
        words = f.read()
        modified_words = words.replace(word, new_word)

    # Count occurrences of the new word
    count = modified_words.count(new_word)

    # Write the modified content back to the file
    with open("data.txt", 'w') as f:
        f.write(modified_words)

    return count

def main():
    word = input("word = ")
    new_word = input("new word = ")

    count = repl(word, new_word)
    print(count)

main()