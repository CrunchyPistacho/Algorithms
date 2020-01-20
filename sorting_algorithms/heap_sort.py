
A = [5,3,4,2,1,10,8,15,22,6]

def parent(x):
   return(x // 2) 

def left(x):
    return(2 * x + 1)

def right(x):
    return(2 * x + 2)

def max_heapipy(x,n,i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and x[i] < x[l]:
        largest = l
    else:
         largest = i
    if r < n and x[r] > x[largest]:
        largest = r
    if largest != i:
        x[i],x[largest] = x[largest],x[i]
        max_heapipy(x,n,largest)

def build_max_heap(x):
    n = len(x)
    for i in range(n, -1, -1):
        max_heapipy(x,n,i)

def heap_sort(x):
    n = len(x)
    build_max_heap(x)
    for i in range(n-1, 0, -1):
        x[i],x[0] = x[0],x[i]
        n = n - 1
        max_heapipy(x,n,0)
    return(x)

print(heap_sort(A))
