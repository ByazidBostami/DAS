import numpy as np 

def create_array():
    rows, cols = 2,3
    m = np.zeros((rows,cols), dtype =int )

    for i in range(rows):
        for j in range(cols):
            m[i][j] = int(input(f"elter element of [{i}][{j}] index: "))

    return m 

result = create_array()
print(f"The created arry is \n{result}")