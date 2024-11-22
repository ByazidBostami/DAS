import numpy as np 

array = list(map(int, input("Please enter a number with comma: ").split(',')))
print(len(array))
print(array)
def leftshift(left):
    for i in range(len(left)-1):
        left[i] = left[i+1]
        
    left[-1] = 0
    
leftshift(array)
print(array)


def rightshift(right):
    i = len(right)-1 # len and index not same , index is 1 less then len
    while i>=0:
        right[i] = right[i-1]
        i -=1
    right[0]=0
rightshift(array)
print(array)

def rightrotation(rr):
    last = rr[-1]
    i = len(rr) - 1
    while i > 0:
        rr[i] = rr[i - 1]
        i -= 1
    rr[0] = last
rightrotation(array)
print(array)

def leftrotation(lr):
    first = lr[0]
    for i in range(len(lr) - 1):
        lr[i] = lr[i + 1]
    lr[-1] = first
    
leftrotation(array)
print(array)