
A = [5,3,4,2,1,10,8,15,22,6]

def bubble_sort(x, ascending = True):
    if ascending == True:
        for i in range(0,len(x)-1):
            for j in range(len(x)-1,i,-1):
                if x[j] < x[j-1]:
                    x[j], x[j-1] = x[j-1], x[j]
    elif ascending == False:
        for i in range(0,len(x)-1):
            for j in range(len(x)-1,i,-1):
                if x[j] > x[j-1]:
                    x[j], x[j-1] = x[j-1], x[j]
    return x

print(bubble_sort(A, ascending=True))