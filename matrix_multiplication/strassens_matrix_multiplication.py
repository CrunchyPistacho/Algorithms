import square_matrix_multiply as smm

A = [[1,2,3,3], [2,2,1,4], [1,3,2,4], [1,1,1,1]]
B = [[1,1,1,1], [1,2,3,2], [0,1,1,3], [1,5,6,4]]

def matrix_dimensions(x):
    return len(x), len(x[0])

def add_matrix(x, y):
    return([[x[row][col] + y[row][col]
            for col in range(len(x[row]))] for row in range(len(x))])


def substract_matrix(x, y):
    return([[x[row][col] - y[row][col]
            for col in range(len(x[row]))] for row in range(len(x))])


def split_matrix(x):
    # This algorithm just works for odd matrix
    if len(x) % 2 != 0 or len(x[0]) % 2 != 0:
        raise Exception("Odd matrices not supported")

    matrix_length = len(x)
    mid = matrix_length // 2
    top_left = [[x[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[x[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    top_right = [[x[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[x[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return(top_left, top_right, bot_left, bot_right)



def strassen(x, y):
    if matrix_dimensions(x) != matrix_dimensions(y):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{x} \nMatrix B:{y}')
    if matrix_dimensions(x) == (2, 2):
        return smm.square_matrix_multiply(x, y)

    A, B, C, D = split_matrix(x)
    E, F, G, H = split_matrix(y)

    p1 = strassen(A, substract_matrix(F, H))
    p2 = strassen(substract_matrix(A, B), H)
    p3 = strassen(add_matrix(C, D), E)
    p4 = strassen(D, substract_matrix(G, E))
    p5 = strassen(add_matrix(A, D), add_matrix(E, H))
    p6 = strassen(substract_matrix(B, D), add_matrix(G, H))
    p7 = strassen(substract_matrix(A, C), add_matrix(E, F))

    top_left = add_matrix(substract_matrix(add_matrix(p5, p4), p2), p6)
    top_right = add_matrix(p1, p2)
    bot_left = add_matrix(p3, p4)
    bot_right = substract_matrix(substract_matrix(add_matrix(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix


print(strassen(A,B))