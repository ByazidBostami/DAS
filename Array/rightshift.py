import numpy as np 
arr = list(map(int, input("Please input something with comma:").split(",")))

def rightshift(rs):
    i = len(rs)-1
    while i>0:
        rs[i] = rs[i-1]
        i-= 1
        
    rs[0] = 0

rightshift(arr)
print(arr)