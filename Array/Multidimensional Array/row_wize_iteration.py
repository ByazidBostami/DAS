import numpy as np 

def create_array():
    rows, cols = 2,3
    m = np.zeros((rows,cols), dtype =int )

    for i in range(rows):
        for j in range(cols):
            m[i][j] = int(input(f"elter element of [{i}][{j}] index: "))

    return m 

def print_row(m):
    rows,cols = m.shape
    

    for i in range(rows):
        for j in range(cols):
            print(m[i][j],end = ',')
        print()


def print_col(m):
    rows,cols = m.shape
    for i in range(cols):
        for j in range(rows):
            print(m[j][i],end = ',')
        print()

result = create_array()
print(f"The created arry is \n{result}")
print(f"Row iteration {print_row(result)}")
print(f"Col iteration {print_col(result)}")