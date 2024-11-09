import numpy as np 
array = np.array([10,20,30,40,50,60])

def rightshift(a):
    
    i = len(a)-1
    while i > 0:
        a[i] = a[i-1]
        i -= 1
    a[0] = 0

rightshift(array)
print(array)