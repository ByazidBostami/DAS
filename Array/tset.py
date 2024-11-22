# def print_matrix(m):
#   row,col = m.shape
#   for i in range(row):
#     c = 1
#     print('|', end='')
#     for j in range(col):
#       c += 1
#       if(len(str(m[i][j])) == 1):
#         print(' ',m[i][j], end = '  |')
#         c += 6
#       else:
#         print(' ',m[i][j], end = ' |')
#         c += 6
#     print()
#     print('-'*(c-col))

import numpy as np
def create_array():
    array = np.array([10,20,30,40,50,60])
    return array


def reverse_out_of_print(arr):
    arr_2 = np.zeros(len(arr) , dtype= int)

    i = 0
    j = len(arr)-1

    while i < len(arr):
        arr_2[i] = arr[j]
        i +=1
        j -=1

    return arr_2

def reverse_inPlace(arr):
    j = len(arr)-1
    for i in range((len(arr))//2):
        arr[j],arr[i] = arr[i],arr[j]
        j = j-1
    return arr

def print_non_dummies_array(arr , size):
    for i in range(size-1):
        print(arr[i], end = ",")




        
a = create_array()
print(f"reverse out {reverse_out_of_print(a)}")
print(f"Reverse in place{reverse_inPlace(a)}")
print_non_dummies_array(a, 5)


