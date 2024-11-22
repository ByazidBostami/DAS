import numpy as np 
array = np.array([10,20,30,40])

def iteration(a):
    i = 0
    while i<len(a):
        print(a[i])
        i+=1
        
iteration(array)


# using for loop 

def iterationforloop(b):
    newar = []
    for i in range(len(b)):
        newar.append(int(b[i]))
        
    return newar
    
print(iterationforloop(array))

def whileloopit(ar):
    i = 0
    while i< len(ar):
        print(ar[i])
        i+=1
whileloopit(array)

