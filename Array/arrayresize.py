# we cann't resize an array 
#we have to create a new array with new index and then copy values from original one 

import numpy as np 
# arr = np.array([10,20,30,40])

# def resize(arr,news):
#     arr2 = [0] * news

#     for i in range(min(len(arr),news)):
#         arr2[i] = arr[i]

#     return arr2

# def resize(arr,news):
#     arr_2 = [0]* news
#     i = 0
#     while i < len(arr):
#         arr_2[i] = arr[i]
#         i+=1
#     return arr_2

# def copyArray(arr):
#     arr_3 = np.zeros(5, dtype=int)
#     for i in range(len(arr)-1):
#         arr_3[i] = arr[i]
#     return arr_3

def resize(arr,new_size):
    arr_1 = [0]*new_size
    i = 0
    while i < len(arr):
        arr_1[i] = arr[i]
        i += 1
    return arr_1

def copyArray(arr):
    arr_2 = np.zeros(len(arr), dtype=int)

    for i in range(len(arr)):
        arr_2[i] = arr[i]
    return arr_2




arr_4 = np.array([9, 8, 7, 6])
copied_array = copyArray(arr_4)
print("Copied Array:", copied_array) 

original_array = [1, 2, 4]
resized_array = resize(original_array, 5)
print("Resized Array:", resized_array)  

original_array_np = np.array(original_array)
copied_array_from_list = copyArray(original_array_np)
print("Copied Array from List:", copied_array_from_list) 

