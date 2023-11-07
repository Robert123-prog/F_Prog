#pune literele dintr un cuvant intr un dictionar si numara numarul de aparenta = vector contor
def count_char(word):
    d = {}

    for ch in word:

        if ch in d:
            d[ch] += 1

        else:
            d[ch] = 1
        # ct = 0
        #
        # for och in word:
        #     if ch == och:
        #         ct += 1

    return d

# word = input("word = ")
# print(count_char(word))

# def add_tag(tag, word): baga tag de html
#     return '<' + tag + '>' + word + '<' + tag + '>'
#
# print(add_tag("ul", "cuv"))


# def palindrom(word):
#     for idx in range(len(word) - 1):
#         if word[idx] != word[-idx - 1]: # sau len(word) - idx - 1
#             # vector[-1] rezulta ultimul el
#             return False
#
#     return True
#
# print(palindrom("abccba"))

#reverse lejer la un string

# def rev(word):
#     return word == word[::-1]
#
# print(rev("salut")) ##idk

# def factorial(n):
#     f = 1
#
#     while n > 1:
#         f *= n
#         n -= 1
#
#     return f
#
# print(factorial(4))

# def car_unice(word):
#     cnt = 0
#
#     for chv in count_char(word).values():
#         if chv == 1:
#             cnt += 1
#
#     return cnt
#
# print(car_unice("school"))


# def anagrame(cuv1, cuv2):
#     l1 = list(cuv1)
#     l2 = list(cuv2)
#     ok = False
#
#     if len(l1) != len(l2):
#         return False
#     else:
#         for ch1 in l1:
#             for ch2 in l2:
#                 if ch1 == ch2:
#                     ok = True
#                     break
#
#     if ok == True:
#         return True
#     else:
#         return False


# pb 6 cu dictionare func
# def anagrame_cudic(cuv1, cuv2):
#     d1 = count_char(cuv1)
#     d2 = count_char(cuv2)
#
#     if d1 == d2:
#         return True
#     else:
#         return False
#
# cuv1 = input("cuv1 = ")
# cuv2 = input(("cuv2 = "))
# #
# print(anagrame(cuv1, cuv2))

