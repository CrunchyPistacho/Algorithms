
A = [[1,2,3], [2,2,1], [1,3,2]]
B = [[1,1,1], [1,2,3], [0,1,1]]

# basic algorithm
def square_matrix_multiply(x,y):
    n = len(x)
    c = [[0 for x in range(n)] for y in range(n)] 
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                    c[i][j] = c[i][j] + x[i][k] * y[k][j]
    return(c)

print(square_matrix_multiply(A,B))