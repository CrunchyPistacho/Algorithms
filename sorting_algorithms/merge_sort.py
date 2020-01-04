
A = [5,3,4,2,1,10,8,15,22,6]
B = [1,3,4,2,5,6]
# x = array with 2 sorted arrays, from [p,q] and [q+1,r]
def merge(x,p,q,r):    
    L = x[p:q]
    R = x[q:r]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p,r):
        print(x)
        if L[i] < R[j]:
            x[k] = L[i]
            i = i + 1
        else:
            x[k] = R[j]
            j = j + 1
    return(x)

def merge_sort(x,p,r):
    print(p)
    print(r)
    if p + 1 < r:
        q = ((p + r) // 2)
        merge_sort(x,p,q)
        merge_sort(x,q,r)
        merge(x,p,q,r)
    return(x)

print(merge_sort(A,0,len(A)))
