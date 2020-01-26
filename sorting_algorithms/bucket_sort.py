from insertion_sort import insertion_sort


A = [0.23,0.33,0.12,0.34,0.68,0.58,0.97]

def bucket_sort(x, slot):
    B = []
    for i in range(slot): 
        B.append([]) 
    for i in x:
        i_b = int(slot * i)
        B[i_b].append(i)
    for j in range(slot):
        B[j] = insertion_sort(B[j])
    return(B)

print(bucket_sort(A,3))