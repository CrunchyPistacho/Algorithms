
A = [5,3,4,2,1,10,8,15,22,6]

def partition(x,p,r):
    y = x[r-1]
    i = p - 1
    for j in range(p,r-1):
        if x[j] <= y:
            i = i + 1
            x[i],x[j] = x[j],x[i]
    x[i+1],x[r-1] = x[r-1],x[i+1]
    return(i+1)

# x = array, p = start, r = end
def quicksort(x,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)
    return(x)


print(quicksort(A,0,len(A)))
print(len(A))
print(A)