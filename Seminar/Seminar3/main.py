# # def find(target, source):
# #     for i in range(len(target) - len(source) + 1):
# #         cnt = 0
# #         idx = i
# #
# #         for j in range(len(source)):
# #             if target[i] == source[j]:
# #                 cnt += 1
# #             idx += 1
# #
# #         if cnt == len(source):
# #             return i
# #
# #     return -1
#
# # def find_better(target, source):
# #     for i in range(len(target) - len(source) + 1):
# #         if target[i:i + len(source)] == source:
# #             return i
# #
# #     return -1
#
# def find_even_better(target, source):
#     position = -1
#     j = 0 #for source; indexul din al doilea sir
#
#     for i in range(len(target)):
#         if target[i] != source[j]:
#             position = -1
#             j = 0
#
#         if target[i] == source[j]:
#             if j == 0:
#                 position = i
#
#         if j >= len(source) - 1:
#             break
#
#         else:
#             j += 1
#
#
#     return position
#
# # def test_find_1():
# #     assert find('string', 'ing') == 3
# #     assert find('stiring', 'ing') == 4
#
# # def test_find_better():
# #     assert find_better('string', 'ing') == 3
# #     assert find_better('stiring', 'ing') == 4
#
# def test_find_even_better():
#     assert find_even_better('string', 'ing') == 3
#     assert find_even_better('stiring', 'ing') == 4
#
# def main():
#     pass
#
# test_find_even_better()
# main()

#ex 2
# def find_sum(numbers, sum):
#     for i in range(len(numbers) - 1):
#
#         if sum - i in numbers:
#             return i, sum - i
#
#     return None
#
# def test_find_sum():
#     assert find_sum([1, 2, 9], 3) == (1, 2)
#     assert find_sum([1, 2, 9], 12) == None
#
# def main():
#     pass

#ex 3

# def generate_multiple(number, count):
#     multi = [number]
#     i = 2
#
#
#     while i <= count:
#         multi.append(number * i)
#         i += 1
#
#     return multi
#
# def test_generate_multiple():
#     assert generate_multiple(3, 4) == [3, 6, 9, 12]
#     assert generate_multiple(2, 4) == [2, 4]
#
# def main():
#     test_generate_multiple()

#ex 4

def big_sum(a, b):
    pass

def test_big_sum():
    assert big_sum('123', '123') == '246'
    assert big_sum(('123', '129')) == '252'
    assert big_sum('999', '101') == '1100'