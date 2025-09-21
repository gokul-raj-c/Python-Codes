#Write a Python Program to Transpose a Matrix.
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

n=int(input("enter no of rows: "))
m=int(input("enter no of columns: "))
arr1 = []
print("Enter matrix 1:")
for i in range(n):
    row = []
    for j in range(m):
        val = int(input("Enter element: "))
        row.append(val)
    arr1.append(row)
print("\nmatrix 1:")
for row in arr1:
    print(row)
result_matrix = transpose_matrix(arr1)
print("\nmatrix:")
for row in result_matrix:
    print(row)