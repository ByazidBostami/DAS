# import numpy as np 

# arr = np.array([11,22,33,44,55,66,77,88]) # 8 value 

# def print_non_dummies(ar,size):
#     for i in range(size):
#         print(ar[i])

# # arr_1 = print_non_dummies(arr, 6)
# # print(arr_1) 

# #inserting at the end 

# def resize_array(arr, new_size):
#     new_ar = np.zeros(new_size, dtype=int)
#     for i in range(len(arr)):
#         new_ar[i] = arr[i]

#     return new_ar

# def insert_at_end(arr,size,elem):
#     if size >= len(arr):  
#         arr = resize_array(arr, len(arr) + 5)
#     arr[size] = elem  
#     return arr

# arr_1 = print_non_dummies(arr, 6)  # Print and get the first 6 elements
# print("Array after slicing:", arr_1)

# # Insert an element at the end
# updated_array = insert_at_end(arr_1, len(arr_1), 10)
# print("Updated Array:", updated_array)

import numpy as np 


# arr = np.array([11, 22, 33, 44, 55, 66, 77, 88])  # 8 values

import numpy as np

def create_array():
    array_nu = np.array([10, 20, 30, 40, 50, 60, 70])
    return array_nu

def print_non_dummies(ar, size):
    print(f"First {size} elements of the array:")
    for i in range(size):
        print(ar[i])
    return ar[:size]

def resize_array(arr, new_size):
    new_arr = np.zeros(new_size, dtype=arr.dtype)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    return new_arr

def insert_at_end(arr, size, elem):
    if size >= len(arr):
        arr = resize_array(arr, len(arr) + 5)
    arr[size] = elem
    return arr

def insert_anywhare(arr, size, index, elem):
    if index < 0 or index > size:
        return "Insertion not possible"
    if size >= len(arr):
        arr = resize_array(arr, len(arr) + 3)
    for i in range(size, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = elem
    return arr


def delete_last_element(arr, size):

    if size == 0 and size > len(arr): # need more research 
        return "Delation not possible"
    else:
        arr[size-1] = 0
        return arr

 
def delete_any_element(arr,size,index):
    if size == 0:
        return "Delelation not possible  "
    
    else:
        for i in range(index,size-1):
            arr[i] = arr[i+1]

        arr[size-1] = 0
        return arr
    





# Main program
array_nu = create_array()
print("Original array:", array_nu)

# Demonstrating `print_non_dummies`
arr_1 = print_non_dummies(array_nu, 5)
print("Array after slicing:", arr_1)

# Demonstrating `insert_at_end`
updated_array = insert_at_end(arr_1, len(arr_1), 10)
print("Updated Array after inserting at end:", updated_array)

# Demonstrating `insert_anywhare`
arr_insert = insert_anywhare(updated_array, len(updated_array), 2, 99)
print("Array after inserting at index 2:", arr_insert)
user = int(input("Please input the index number you want to delete :"))
print(f"Delete last element {delete_last_element(array_nu, user)}")
delete_any_element(array_nu,5,2)
print(f"Delete any element : {array_nu}")
