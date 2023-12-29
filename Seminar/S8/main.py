#l = [[1, 2, 3, 4] , [4, 5, 1], [7, 8, 5, 1, 4, 1, 1]]

# def aufg2(list):
#
#     d = {}
#     newl = []
#
#     for l in list:
#         for el in l:
#             if el in d:
#                 d[el] += 1
#
#             else:
#                 d[el] = 1
#
#     for k,v in d.items():
#         for l in list:
#             c = l.count(k) - 1
#
#         if c > 0:
#             v -= c
#
#         if v == len(list):
#             newl.append(k)
#
#     return newl

# def aufg2_2(list):
#     nl = []
#     for el in list[0]:
#         cnt = 0
#         for l in list[1:]:
#
#             if el in l:
#                 cnt += 1
#
#         if cnt == len(list) - 1:
#             nl.append(el)
#
#     return nl
#
# print(aufg2_2(l))


'''
def test():
    assert do_stuff([2, 4, 9]) == [False, False, False]
    assert do_stuff([2, 4, 9]) == [True, True, False]
'''

# def read_matrix(filename):
#     f = open(filename, 'r')
#     matrix = [[int(i) for i in line.strip().split(',')]for line in f]
#     f.close()
#     return matrix
#
# m = read_matrix('input.txt')
#
# def is_sparse(matrix):
#     ct1 = sum([sum(i) for i in matrix])
#     ct0 = len([matrix[i][j] for i in range(len(matrix))for j in range(len(matrix)) if matrix[i][j] == 0])
#
#     # for line in matrix:
#     #     for elem in line:
#     #         if elem == 1:
#     #             ct1 += 1
#     #
#     #         if elem == 0:
#     #             ct0 += 1
#
#
#
#     return ct0 > 0.7 * (ct1 + ct0)
#
#
# print(is_sparse(m))


#implementarea mea la prob 2, primu model de partial
l = [[1, 2, 3, 4] , [4, 5, 1], [7, 8, 5, 1, 4, 1, 1], [1, 1, 1, 4, 5, 10, 14], [1, 4, 5], [4, 4, 1, 1, 4, 1, 4]]

l1 = [1, 2, 3, 4]
l2 = [4, 5, 1]
def comm_elements(l1, l2):
    nl = []

    for i in l1:

        for j in l2:

            if i == j and j not in nl:
                nl.append(i)

    return nl


def choose_comm(l):
    nl = []
    l1 = []
    l2 = []

    for ind in range(0, len(l) - 1, 2):

        if len(nl) == 0:
            l1 = l[ind]
            l2 = l[ind + 1]
            nl = comm_elements(l1, l2)

        else:
            l1 = nl
            l2 = l[ind + 1]
            nl = comm_elements(l1, l2)

    return nl

print(choose_comm(l))