m = [['A', 'B', 'C', 'D'],
     ['L', 'E', 'G', 'H'],
     ['Q', 'R', 'T', 'F']]

word = 'ALERT'

l = list(word)
ct = len(l)

def find(m, word):
    t = 0

    for i in word:

        for j in m:

            for k in j:

                if i == k:

                    t += 1
    if t == ct:
        return True

    else:
        return False


def main():

    print(find(m, word))

main()

