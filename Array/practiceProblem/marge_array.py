import numpy as np
def marge_array(arr,arr_01,size_01,size_02):
    total_size = size_01 + size_02
    marge_array = np.zeros(total_size, dtype=int)

    for i in range (total_size):
        if i < size_01:
            marge_array[i] = arr[i]
        else:
            marge_array[i] = arr_01[i-size_01]


    return marge_array

arr1 = np.array([1,5,0,0])
arr2 = np.array([3,5,2])

print(marge_array(arr1,arr2,2,3))

# arr1 = [1, 5]       # size1 = 2
# arr2 = [3, 5, 2]    # size2 = 3
# merged_array = [0, 0, 0, 0, 0]  # total_size = size1 + size2 = 5

# # Loop to fill merged_array:
# # i = 0, i < size1 --> merged_array[0] = arr1[0] = 1
# # i = 1, i < size1 --> merged_array[1] = arr1[1] = 5
# # i = 2, i >= size1 --> merged_array[2] = arr2[2 - size1] = arr2[0] = 3
# # i = 3, i >= size1 --> merged_array[3] = arr2[3 - size1] = arr2[1] = 5
# # i = 4, i >= size1 --> merged_array[4] = arr2[4 - size1] = arr2[2] = 2

# # Final merged_array: [1, 5, 3, 5, 2]
