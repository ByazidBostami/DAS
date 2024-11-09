# import numpy as np
# arr = np.zeros(4)
# zeros = [1,2,3,4]
# print(zeros)

# arr2 = np.array([1,2,3,4,5,9])
# print(arr2)

import numpy as np 

array = np.array([1,2,3,4,5])

def leftsift(array):
    i = 1
    while i < len(array):
        array[i-1] = array[i]
        i += 1
 
    array[len(array)-1] = 0

leftsift(array)
print(array)
    