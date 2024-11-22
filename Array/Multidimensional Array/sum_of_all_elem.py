import numpy as np 

def create_array():
    rows, cols = 3,4
    m = np.zeros((rows,cols), dtype =int )

    for i in range(rows):
        for j in range(cols):
            m[i][j] = int(input(f"elter element of [{i}][{j}] index: "))

    return m 
def array_sum(m):
    sum = 0
    rows,cols = m.shape
    for i in range(rows):
        for j in range(cols):
            sum = sum + m[i][j]

    return sum 

def row_wise_sum(m):
    sum = 0
    r,c = m.shape
    result = np.zeros((r,1),dtype=int)

    for i in range(r):
        for j in range(c):
            result[i][0] += m[i][j]

    return result

def col_wise_sum(m):
    r,c = m.shape
    result = np.zeros((1,c),dtype = int)
    for i in range(c):
        for j in range(r):
            result [0][i] += m[j][i]

    return result

result = create_array()
print(f"Main array {result}")
print(f"total sum: {array_sum(result)}")
print(f"total row: {row_wise_sum(result)}")

"""

Loop Iterations:
First Row (i = 0):

j = 0: result[0][0] = result[0][0] + m[0][0] = 0 + 1 = 1
j = 1: result[0][0] = result[0][0] + m[0][1] = 1 + 2 = 3
j = 2: result[0][0] = result[0][0] + m[0][2] = 3 + 3 = 6
After completing row i = 0: result = [[6], [0]]

Second Row (i = 1):

j = 0: result[1][0] = result[1][0] + m[1][0] = 0 + 4 = 4
j = 1: result[1][0] = result[1][0] + m[1][1] = 4 + 5 = 9
j = 2: result[1][0] = result[1][0] + m[1][2] = 9 + 6 = 15
After completing row i = 1: result = [[6], [15]]
"""