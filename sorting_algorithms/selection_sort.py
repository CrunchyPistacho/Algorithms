
A = [5,3,4,2,1,10,8,15,22,6]

def selection_sort(x, ascending = True):
    if ascending == True:
        for j in range(0,len(x)):
            key = j
            for i in range(j,len(x)):
                if x[key] > x[i]:
                    key = i
            x[j], x[key] = x[key], x[j]
        return(x)
    elif ascending == False:
        for j in range(0,len(x)):
            key = j
            for i in range(j,len(x)):
                if x[key] < x[i]:
                    key = i
            x[j], x[key] = x[key], x[j]
        return(x)

print(selection_sort(A))
print(selection_sort(A, ascending = False))