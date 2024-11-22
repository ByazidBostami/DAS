import numpy as np 

def create_array():
    rows, cols = 2,2
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

def swap_row(m):
    rows,cols = m.shape
    for i in range(rows ):
        temp = m[i][0]
        m[i][0] = m[i][1]
        m[i][1] = temp
    return m 

def swap_col(m):
    r,c = m.shape
    for i in range(r):
        for j in range(c//2):
            temp = m[i][j]
            m[i][j] = m[i][c-1-j]
            m[i][c-1-j] = temp

    return m
def sum_primary_diagonal(m):
    r,c = m.shape

    # assert r == c ,"Not a square matrix"
    sum = 0
    for i in range(r):
        sum += m[i][i]
    return sum

def add_matrix(m1,m2):
    rows1, cols1 = len(m1),len(m1[0])
    rows2, cols2 = len(m2),len(m2[0])

    # assert rows1 == rows2 and cols1 == cols2, "Matrix must have same dimention "

    result = np.zeros((rows1, cols1), dtype=int)
    for i in range(rows1):
        for j in range(cols1):
            result [i][j] = m1[i][j] + m2[i][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrix(matrix1, matrix2)
print("Resultant Matrix:")
for row in result:
    print(row)    

result = create_array()
print(f"Main array {result}")
print(f"total sum: {array_sum(result)}")
print(f"total row: {row_wise_sum(result)}")
print(f"total col: {col_wise_sum(result)}")
print(f"Swap row :{swap_row(result)}")
print(f"Col swap {swap_col(result)}")
print(f"Sum of square matrix: {sum_primary_diagonal(result)}")

"""
example for understand 
m = [[1, 2, 3], 
     [4, 5, 6]]
result = [[0], 
          [0]]

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
"""
Let me explain this part step by step. The three lines of code perform a **swap** between two elements in the same row of a 2D array.

---

### Code in Context:
```python
temp = m[i][j]
m[i][j] = m[i][c - 1 - j]
m[i][c - 1 - j] = temp
```

This is part of a **column-swapping operation**. It swaps the element at column `j` with the element at column `c - 1 - j` in the same row `i`.

### Variables:
1. **`m[i][j]`:**
   - Represents the element in row `i` and column `j`.

2. **`m[i][c - 1 - j]`:**
   - Represents the element in row `i` but in the **mirrored column** on the other side of the row.

   - For example:
     - If the row has 4 columns (`c = 4`) and `j = 0`, then `c - 1 - j = 3`. So `m[i][0]` swaps with `m[i][3]`.

3. **`temp`:**
   - A temporary variable used to hold the value of `m[i][j]` during the swap so it’s not overwritten.

---

### How It Works:
1. **Step 1: Store `m[i][j]` in `temp`**
   ```python
   temp = m[i][j]
   ```
   - This saves the current value of `m[i][j]` (so it’s not lost when we overwrite `m[i][j]`).

2. **Step 2: Assign the mirrored column value to `m[i][j]`**
   ```python
   m[i][j] = m[i][c - 1 - j]
   ```
   - The value from column `c - 1 - j` is placed in column `j`.

3. **Step 3: Assign the stored value (`temp`) to `m[i][c - 1 - j]`**
   ```python
   m[i][c - 1 - j] = temp
   ```
   - The value stored in `temp` (the original value of `m[i][j]`) is placed in the mirrored column.

---

### Example Walkthrough:
Given the 2D array:
```plaintext
[[1, 2, 3, 4]]
```

1. **Setup:**
   - `i = 0` (processing the first and only row).
   - `c = 4` (number of columns).

2. **First Inner Loop (`j = 0`):**
   - `m[0][j] = m[0][0] = 1`
   - `m[0][c - 1 - j] = m[0][3] = 4`

   **Swap Steps:**
   - `temp = m[0][0] = 1`
   - `m[0][0] = m[0][3] = 4`
   - `m[0][3] = temp = 1`

   **Result after swap:**
   ```plaintext
   [[4, 2, 3, 1]]
   ```

3. **Second Inner Loop (`j = 1`):**
   - `m[0][j] = m[0][1] = 2`
   - `m[0][c - 1 - j] = m[0][2] = 3`

   **Swap Steps:**
   - `temp = m[0][1] = 2`
   - `m[0][1] = m[0][2] = 3`
   - `m[0][2] = temp = 2`

   **Result after swap:**
   ```plaintext
   [[4, 3, 2, 1]]
   ```

---

### Why is `temp` Needed?
Without `temp`, the original value of `m[i][j]` would be lost when `m[i][j]` is overwritten:
```plaintext
m[i][j] = m[i][c - 1 - j]  # Overwrites the value at m[i][j]
```

Using `temp`, you can safely store the original value of `m[i][j]` and assign it to the mirrored position later.

---

### Final Outcome:
This swapping process mirrors the columns of the matrix for each row.

Example:
```plaintext
Input:
[[1, 2, 3, 4],
 [5, 6, 7, 8]]

Output:
[[4, 3, 2, 1],
 [8, 7, 6, 5]]
```

"""