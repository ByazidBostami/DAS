import numpy as np 
array = np.array(["m","a","d","a","m"])

def check_palindrome(arr):
    arr_2 = np.zeros(len(arr), dtype=str)

    i = 0
    j = len(arr)-1
    while i < len(arr):
        arr_2[j] = arr[i]
        i += 1
        j -= 1
    print(arr_2)    

    if np.array_equal(arr,arr_2):
        return "Palindrome"
    else:
        return "Not a palindrome"

test = check_palindrome(array)
print(test)