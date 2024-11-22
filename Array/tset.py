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

def resize_array(arr, new_size):
    arr_2 = np.zeros(new_size , dtype=int)
    i = 0 
    while i <len(arr):
        arr_2[i] = arr[i]
        i += 1

    return arr_2

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


def inser_at_the_end(arr, size, elem):
    if size > len(arr):
        arr = resize_array(arr, len(arr)+5)

    arr[size] = elem
    return arr


def insert_anywhere(arr, size,index,elem):
    if index <0 or index> size:
        return "Insertion not possible "
    
    if size >= len(arr):
        arr = resize_array(arr, len(arr)+5)
    for i in range(size,index,-1):
        arr[i] = arr[i-1]
    arr[index] = elem

    return arr 

def delete_last_element(arr,size):
    if size == 0 :
        return "Deletion not possible"
    arr[size-1] = 0
    return arr

def delete_any_element(arr,size,index):
    if size == 0:
        return "Deletion not possible"
    for i in range(size,index,-1):
        arr[i] = arr[i+1]
    arr[size-1] = 0
    return arr
        
a = create_array()



print(f"Resized array {resize_array(a,10)}")
print(f"reverse out {reverse_out_of_print(a)}")
print(f"Reverse in place{reverse_inPlace(a)}")
print_non_dummies_array(a, 5)
print(f"insert at end {inser_at_the_end(a, 5,244)}")
print(f"Inseart anywhere {insert_anywhere(a,5,2,255)}")
print(f"Last element delete {delete_last_element(a,6)}")
print(f"Any element Delation {delete_any_element(a,3,7)}")


