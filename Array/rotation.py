import numpy as np

array = np.array([10,20,30,40,50,60,70])

def rotation(r):
    temp = r[len(r)-1]
    i = len(r)
    while i < len(r):
        r[i-1] = r[i]
        i += 1

    r[0]= temp
    return r 

rotation(array)
print(array)
