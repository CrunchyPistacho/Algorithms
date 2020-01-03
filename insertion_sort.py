# imput array

A = [5,3,4,2,1,10,8,15,22,6]

def insertion_sort(x, ascending = True):
    if ascending == True: 
        for j in range(1,len(x)):
            key = x[j]
            i = j - 1
            while i >= 0 and x[i] > key:
                x[i + 1] = x[i]
                i = i - 1
            x[i + 1] = key
    elif ascending == False:
        for j in range(1,len(x)):
            key = x[j]
            i = j - 1
            while i >= 0 and x[i] < key:
                x[i + 1] = x[i]
                i = i - 1
            x[i + 1] = key    
    return(x)

print(insertion_sort(A))
print(insertion_sort(A, ascending = False))