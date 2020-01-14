# Calculate the maximum distance between 2 elements of the same array.
# Imput shoud be a difference between values array
A = [5,3,4,2,1,10,8,15,22,6]
B = [-2,1,-2,-1,9,-2,7,7,-16]

def max_crossing_subarray(x,low,mid,hight):
    left_sum = -float('inf')
    max_left = max_right = min(x[low:hight])-1
    s = 0
    for i in range(mid - 1, low - 1, -1):
        s = s + x[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -float('inf')
    s = 0
    for j in range(mid, hight):
        s = s + x[j]
        if s > right_sum:
            right_sum = s
            max_right = j
    return(max_left,max_right,left_sum + right_sum)

def find_maximum_subarray(x, low, hight):
    if(low == hight-1):
        return (low, hight, x[low])
    else:
        mid = int((low+hight)/2)
        Left_Low, Left_High, Left_Max = find_maximum_subarray(x, low, mid)
        Right_Low, Right_High, Right_Max = find_maximum_subarray(x, mid, hight)
        Cross_Low, Cross_High, Cross_Max = max_crossing_subarray(x, low, mid, hight)
        if(Left_Max > Right_Max and Left_Max > Cross_Max):
            return (Left_Low, Left_High, Left_Max)
        elif(Right_Max > Left_Max and Right_Max > Cross_Max):
            return(Right_Low, Right_High, Right_Max)
        else:    
            return (Cross_Low, Cross_High, Cross_Max)

print(max_crossing_subarray(B,0,int(len(B)/2),len(B)))

print(find_maximum_subarray(B,0,len(B)))
