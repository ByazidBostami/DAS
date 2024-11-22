import numpy as np
def create_array():
    array = np.array([1,3,2,5,0,0])

    return array

def resize_array(arr, new_size):
    arr_2 = np.zeros(new_size , dtype=int)
    for i in range(new_size):
        if i < len(arr):
            arr_2[i] = arr[i]


    return arr_2

def non_dummy_reverse(arr,size):
    arr = resize_array(arr, size)


    arr_1 = np.zeros(size, dtype=int) 
    
    for i in range(size):
        arr_1[size-i-1] = arr[i] #4-0-1 =3, 4-1-1= 2,4-2-1=1

    

    return arr_1

a = create_array()

print(non_dummy_reverse(a,4))