import numpy as np 
#Method 1
array = [1,2,3,4,5]
print(array)

#method 2
array_1 = list(map (int, input("Enter numbers spearated by comma: ").split(','))) 
print(array_1)


#method 3

array_3 = np.array([1,2,3,4,5])
print(array_3)

#method 4
array_4 = np.zeros(4, dtype=int) # just take a location 
print(array_4)

#method 5 2D 
rows = int(input("Enter number of rows: "))
array_5 = []
for i in range(rows):
    row = list(map(int, input("Enter row values separated by comma; ").split(',')))
    array_5.append(row)
print(array_5)

