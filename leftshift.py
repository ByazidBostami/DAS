import numpy as np
# array = np.array([1,2,3,4,5,6,7])

# def leftshift(a):
#     i = 1
#     while i < len(a):
#         a[i-1] = a[i]
#         i += 1
#     a[len(a)-1] = 0
     
# leftshift(array)
# print(array) 
  
arr = np.array([10,20,30,40,50,60])

def leftshift(lf):
    
    for i in range(len(lf)-1):
        lf[i] = lf[i+1]
    lf[len(lf)-1] = 0
    
leftshift(arr)
print(arr)