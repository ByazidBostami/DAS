import numpy as np 
rows = int(input("Please input row for your 2d array: "))

array_2d = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} element separated by comma: ").split(",")))
    array_2d.append(row)
    
array_2d = np.array(array_2d)

print(f"2D array \n {array_2d}")





# # Taking the number of rows and columns as input
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# # Initializing an empty list to store rows
# array_2d = []

# # Taking each row as input with a validation check
# for i in range(rows):
#     while True:
#         row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
#         if len(row) == cols:
#             array_2d.append(row)
#             break
#         else:
#             print(f"Please enter exactly {cols} elements.")

# # Converting list of lists to a NumPy array
# array_2d = np.array(array_2d)
# print("2D Array:")
# print(array_2d)
