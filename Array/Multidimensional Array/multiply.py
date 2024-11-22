import numpy as np
def multiply (m1,m2):
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])

    # assert cols1 == rows1, "cann't multipy"

    result = np.zeros((rows1,cols1), dtype=int)
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m1[i][k] * m2[k][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply(matrix1, matrix2)

print("Resultant Matrix:")
for row in result:
    print(row)