import numpy as np
array = np.array([1,2,3,4,5,6,7])

def leftshift(a):
    i = 1
    while i < len(a):
        a[i-1] = a[i]
        i += 1
    a[len(a)-1] = 0
     
leftshift(array)
print(array)
