
A = [5,3,4,2,1,10,8,15,22,6]

def counting_sort(x):
    k = max(x)
    c = [0] * (k + 1)
    B = [0] * (len(x))
    for j in x:
        c[j] += 1
    for i in range(1, k+1):
        c[i] = c[i] + c[i - 1]
    for j in range(len(x)-1,-1,-1):
        B[c[x[j]]-1] = x[j]
        c[x[j]] = c[x[j]] -1
    return(B)

print(counting_sort(A))