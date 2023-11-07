# def check_rel1(nr):
#     rel1 = "x = y * 3"
#
#     x = (nr // 10) % 10
#     y = nr % 10
#
#     if x == y * 3:
#         return True
#
#     else:
#         return False
#
#
# def filter(vect):
#
#     lsorted = []
#
#     for i in vect:
#
#         if check_rel1(i) == True:
#
#             lsorted.append(i)
#
#     return lsorted
#
# def list_to_string(vect):
#
#     result = ' '.join(map(str, vect))
#     return result
#
# def main():
#
#     l = [31, 10, 62, 11, 22, 93]
#     print(list_to_string(filter(l)))
#
# main()
#
#
#

def check_rel2(nr):
    rel1 = "x // y = 2"

    x = (nr // 10) % 10
    y = nr % 10

    if x // y == 2:
        return True

    else:
        return False

def filter(vect):

    lsorted = []

    for i in vect:

        if check_rel2(i) == True:

            lsorted.append(i)

    return lsorted

def list_to_string(vect):

    result = ' '.join(map(str, vect))
    return result

def main():

    l = [21, 43, 42, 55, 63, 84, 91]
    print(list_to_string(filter(l)))

main()