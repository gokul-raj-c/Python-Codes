# Write a Python Program to Multiply Two Matrices.
def multiply_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    if cols1 != rows2:
        print("Matrix multiplication is not possible")
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

n=int(input("enter no of rows: "))
m=int(input("enter no of columns: "))
arr1 = []
arr2 = []

print("Enter matrix 1:")
for i in range(n):
    row = []
    for j in range(m):
        val = int(input("Enter element: "))
        row.append(val)
    arr1.append(row)

print("Enter matrix 2:")
for i in range(n):
    row = []
    for j in range(m):
        val = int(input("Enter element: "))
        row.append(val)
    arr2.append(row)

print("\nmatrix 1:")
for row in arr1:
    print(row)

print("\nmatrix 2:")
for row in arr2:
    print(row)

result_matrix = multiply_matrices(arr1, arr2)
print("\nmatrix:")
for row in result_matrix:
    print(row)