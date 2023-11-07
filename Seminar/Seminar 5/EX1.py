#pune matrice de j si i la suma



def check_matrix(matrix):

   for i in range(len(matrix)):
      s = 0

       for j in range(len(matrix[i])):
           s += matrix[j][i]




def test_check_matrix():
    assert check_matrix([
        [4, 3, 10],
        [1, 2, 10],
        [1, 1, 8]
    ]) == True

def sum_of_div(nr):
    s = 0
    d = 1

    while d < nr:
        if nr % d == 0:
            s += d

        d += 1

    return s



def perf_num(num):
    if num == sum_of_div(num):
        return True
    else:
        return False

def main():
    check_matrix([
        [4, 3, 10],
        [1, 2, 10],
        [1, 1, 8]
    ])

main()