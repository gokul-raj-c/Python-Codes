# Write a Python Program to Add Two Matrices.
def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices must have the same dimensions for addition")
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
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

result_matrix = add_matrices(arr1, arr2)
print("\nmatrix:")
for row in result_matrix:
    print(row)