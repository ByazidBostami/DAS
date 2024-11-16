import numpy as np 

arr = np.array([11,22,33,44,55,66,77])

def reverse_out_of_the_place(arr):
    arr_2 = np.zeros(len(arr), dtype=int)
    i = 0
    j = len(arr)-1
    while i<= len(arr)-1:
        arr_2[i] = arr[j] # append value from last order 
        i +=1
        j -=1
    return arr_2

arr_reverse = reverse_out_of_the_place(arr)
print(arr_reverse)

#swap method 

arr_5 = np.array([00,11,22,33,4433])
def reverse_in_place(ar):
    j = len(ar)-1
    for i in range(len(ar)//2):
        ar[i], ar[j] = ar[j], ar[i]
        j -=1

    return ar 
arr_2 = reverse_in_place(arr_5)
print(arr_2)
